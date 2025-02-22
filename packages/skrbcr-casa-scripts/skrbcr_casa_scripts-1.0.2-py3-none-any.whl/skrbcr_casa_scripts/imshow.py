import os
import numpy as np
from matplotlib.patches import Ellipse
import matplotlib.pyplot as plt
from scipy.ndimage import zoom
from .Image import Image
from .PlotConfig import PlotConfig
from .utilities import unitDict, get_pret_dir_name
from .matplotlib_helper import set_cbar, set_axes_options
from .prepare_image import prepare_image


def draw_beam(ax: plt.Axes, img: Image = None, beam: tuple = None, color: str = 'white') -> None:
    """
    Draws the beam on the image.

    Args:
        ax (plt.Axes): The Axes object.
        img (Image): The Image object.
        beam (tuple): The beam parameters (beam_x, beam_y, beam_ang).
                      If both img and beam are provided, beam will be used.
        color (str): The color of the beam. Default to 'white'.
    """
    x_min, x_max = ax.get_xlim()
    y_min, y_max = ax.get_ylim()
    beam_pos_x = x_min + (x_max - x_min) / 8
    beam_pos_y = y_min + (y_max - y_min) / 8
    if img is not None and img.beam:
        beam_x = img.beam_x / np.abs(img.incr_x)
        beam_y = img.beam_y / np.abs(img.incr_y)
        beam_ang = img.beam_ang
    elif beam is not None:
        beam_x, beam_y, beam_ang = beam
    else:
        print('This image does not have a beam.')
        return
    ellipse = Ellipse(xy=(beam_pos_x, beam_pos_y), width=beam_x, height=beam_y, angle=90+beam_ang, 
                      facecolor=color, edgecolor=color)
    ax.add_patch(ellipse)


def imshow(ax: plt.Axes, img: Image, config: PlotConfig = None):
    """
    Rasterizes an image on given Axes object with matplotlib from a CASA style image file.

    Args:
        ax (plt.Axes): The Axes object.
        img (Image): The Image object.
        config (PlotConfig): The PlotConfig object.

    Returns:
        matplotlib.image.AxesImage: The AxesImage object.
    """
    if config is None:
        config = PlotConfig()
    # imagename, img, config = prepare_image(imagename, **kwargs)
    img.convert_axes_unit(config.axesunit)
    # plot
    if not config.show or img.is_cube:
        plt.ioff()

    # Preparatoin for the cube
    if img.is_cube and config.cbar == 'common':
        if config.vmin is None:
            config.vmin = np.nanmin(img.img)
        if config.vmax is None:
            config.vmax = np.nanmax(img.img)

    # Specify the channel
    if config.chan is None:
        id_hz = 0
    else:
        id_hz = config.chan

    # Draw the image
    if img.is_cube:
        im = ax.imshow(img.img[id_hz], cmap=config.cmap, aspect='equal', vmin=config.vmin, vmax=config.vmax, origin='lower')
    else:
        im = ax.imshow(img.img, cmap=config.cmap, aspect='equal', vmin=config.vmin, vmax=config.vmax, origin='lower')

    # Draw the beam
    draw_beam(ax=ax, img=img, color=config.cbeam)

    # Set the title
    if config.title is None:
        config.title = ''

    # Set the axes options
    set_axes_options(ax, config.title, img.axisname_x + f'[{unitDict[img.axis_unit_x]}]', 
                     img.axisname_y + f'[{unitDict[img.axis_unit_y]}]',
                     *img.get_ticks(config.xtickspan, config.ytickspan, config.relative, config.ticksfmt))

    # Set the colorbar
    if config.cbarunit is None:
        config.cbarunit = img.im_unit
    set_cbar(im, config.cbarquantity, config.cbarunit, config.rescale, config.cbarfmt, ':.2f')

    return im


def overlay_contour(ax: plt.Axes, img_base: Image, img: Image, fill=False, nchan=None, **kwargs) -> None:
    """
    Overlays contours on the image.

    To plot with correct scaling, both Image objects should have `incr_x` and `incr_y` attributes.

    Args:
        ax (plt.Axes): The Axes object.
        img_base (Image): Image plotted as background (This should have been already plotted).
        img (Image): Image to be plotted as contours.
        fill (bool): If `True`, the contours will be filled. Default is `False`.
        nchan (int): The channel number to be plotted. If img is a cube, this should be specified.
        **kwargs: Contour configuration keywords of matplotlib.pyplot.contour.
    """
    try:
        height, width = ax.get_images()[0].get_array().shape
    except IndexError:
        print('The background image is not plotted yet. Please plot the background image first.')
        return

    if img.is_cube and nchan is None:
        print('The channel number should be specified for the cube image.')
        return

    img.convert_axes_unit(img_base.axis_unit_x)

    data = img.img[nchan] if img.is_cube else img.img

    ratio = (abs(img.incr_x / img_base.incr_x), abs(img.incr_y / img_base.incr_y))
    data = zoom(data, ratio, order=1)
    # trim the data to the size of the background image by the center
    if data.shape[0] > height:
        diff = data.shape[0] - height
        data = data[diff//2:diff//2+height]
    if data.shape[1] > width:
        diff = data.shape[1] - width
        data = data[:, diff//2:diff//2+width]

    # xlim = ax.get_xlim()
    # ylim = ax.get_ylim()
    # extent = ax.get_images()[0].get_extent()

    # x = np.linspace(extent[0], extent[1], data.shape[1])
    # y = np.linspace(extent[2], extent[3], data.shape[0])
    # X, Y = np.meshgrid(x, y)

    if fill:
        ax.contourf(data, origin='lower', **kwargs)
    else:
        ax.contour(data, origin='lower', **kwargs)
    # ax.contour(data, **kwargs)
    # ax.set_xlim(xlim)
    # ax.set_ylim(ylim)


def lazy_raster(imagename: str, **kwargs) -> None:
    """
    Rasterizes an image with matplotlib from a CASA style image file.
    With this function, you can get an pretty image with a few lines of code.

    Args:
        imagename (str): CASA style image file.
        **kwargs: Plot configuration keywords. Please see PlotConfig for more details.
    """
    imagename, img, config = prepare_image(imagename, **kwargs)
    # plot
    if not config.show or img.is_cube:
        plt.ioff()

    # Preparatoin for the cube
    if img.is_cube and config.cbar == 'common':
        if config.vmin is None:
            config.vmin = np.nanmin(img.img)
        if config.vmax is None:
            config.vmax = np.nanmax(img.img)

    # Specify the channel
    if config.chan is None:
        id_hz = 0
    else:
        id_hz = config.chan

    fig, ax = plt.subplots(figsize=(8, 6))

    # Draw the image
    if img.is_cube:
        im = ax.imshow(img.img[id_hz], cmap=config.cmap, aspect='equal', vmin=config.vmin, vmax=config.vmax, origin='lower')
    else:
        im = ax.imshow(img.img, cmap=config.cmap, aspect='equal', vmin=config.vmin, vmax=config.vmax, origin='lower')

    # Draw the beam
    draw_beam(ax=ax, img=img, color=config.cbeam)

    # Set the title
    if config.title is None:
        config.title = imagename

    # Set the axes options
    set_axes_options(ax, config.title, img.axisname_x + f'[{unitDict[img.axis_unit_x]}]', 
                     img.axisname_y + f'[{unitDict[img.axis_unit_y]}]',
                     *img.get_ticks(config.xtickspan, config.ytickspan, config.relative, config.ticksfmt))

    # Set the colorbar
    if config.cbarunit is None:
        config.cbarunit = img.im_unit
    set_cbar(im, config.cbarquantity, config.cbarunit, config.rescale, config.cbarfmt, ':.2f')
    fig.tight_layout()

    # Save the figure
    savename = config.savename
    if savename is not None:
        if savename == '':
            savename = imagename
        if img.is_cube:
            savename += f'-{id_hz}'
        savename += '.png'
        fig.savefig(savename, dpi=config.dpi)
        print(f'Saved as "{savename}"')
    if config.show:
        plt.show()
