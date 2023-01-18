import numpy as np
import seaborn as sns
from scipy import stats
import matplotlib.pyplot as plt
import random
from matplotlib.colors import ListedColormap, LinearSegmentedColormap


def hex_to_rgb(value):
    """
    Converts hex to rgb colours
    value: string of 6 characters representing a hex colour.
    Returns: list length 3 of RGB values"""
    value = value.strip("#")  # removes hash symbol if present
    lv = len(value)
    return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))


def rgb_to_dec(value):
    """
    Converts rgb to decimal colours (i.e. divides each value by 256)
    value: list (length 3) of RGB values
    Returns: list (length 3) of decimal values
    """
    return [v/256 for v in value]


def get_continuous_cmap(hex_list, float_list=None):
    """ 
    Creates and returns a color map that can be used in heat map figures.
    If float_list is not provided, colour map graduates linearly between each color in hex_list.
    If float_list is provided, each color in hex_list is mapped to the respective location in float_list.

    Parameters
    ----------
    hex_list: list of hex code strings
    float_list: list of floats between 0 and 1, same length as hex_list. Must start with 0 and end with 1.

    Returns
    ----------
    colour map
    """
    rgb_list = [rgb_to_dec(hex_to_rgb(i)) for i in hex_list]
    if float_list:
        pass
    else:
        float_list = list(np.linspace(0, 1, len(rgb_list)))

    cdict = dict()
    for num, col in enumerate(['red', 'green', 'blue']):
        col_list = [[float_list[i], rgb_list[i][num], rgb_list[i][num]]
                    for i in range(len(float_list))]
        cdict[col] = col_list
    cmp = LinearSegmentedColormap('my_cmp', segmentdata=cdict, N=256)
    return cmp


def gaussian_smooth(x, y, sd=1):
    """
    Function to apply a gaussian filter to the passed function

    Args:
        x (np.array): x_values for the function
        y (np.array): y_values for the function
        sd (float, optional): Standard deviation of the kernel in pixel units.

    Returns:
        np.array: smoothed y_values
    """
    weights = np.array([stats.norm.pdf(x, m, sd) for m in x])
    weights = weights / weights.sum(1)
    return (weights * y).sum(1)


def set_plot_features(fig, ax, text_size=10, line_width=2, tick_param=1.5, axis='both', optim_text=True, show_legend=True):
    """
    Function to improve the visual effects of plotted figure.
    Args:
        fig (Figure): figure to modify.
        ax (Axes): ax to modify.
        text_size (int, optional): Text size for the tick parameters. Defaults to 8.
        line_width (int, optional): Line width. Defaults to 2.
        tick_param (float, optional): Tick width in points. Defaults to 1.5.
        axis (str, optional): Tick width in points. Defaults to 'both'.
        optim_text (bool, optional): automatically calculate the best text size for the tick parameters. Defaults to True.
        show_legend (bool, optional): show legend in plot. Defaults to True
    """

    if optim_text:
        size = fig.get_size_inches()*fig.dpi
        min_text = 8
        max_test = 20
        text_size = (size[0] + size[1])/100
        if text_size < min_text:
            text_size = min_text
        if text_size > max_test:
            text_size = max_test

    if axis == 'both':
        ax.tick_params(axis='x', labelsize=text_size)
        ax.tick_params(axis='y', labelsize=text_size)
    elif axis == 'x' or axis == 'y':
        ax.tick_params(axis=axis, labelsize=text_size)
    else:
        print('Wrong axis for tick parameters')
        exit()

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_linewidth(line_width)
    ax.spines['left'].set_linewidth(line_width)

    ax.xaxis.set_tick_params(width=tick_param)
    ax.yaxis.set_tick_params(width=tick_param)

    if show_legend:
        plt.legend(fontsize=text_size)


def create_stack_plot(fig, ax, df, x_column, y_column, colors=[], filter_size=10, text_size=8, optim_text=True):
    """
    Create a gaussian filtered stacked plot 

    Args:
        fig (Figure): figure to modify.
        ax (Axes): ax to modify.
        df (DataFrame): DataFrame with the grouped data.
        x_column (str): column of data to be used for x label 
        y_columns (list, str): column/s of data to stack. Can be both list of string based on the need.
        colors (list, optional): list of colors to use for hue of the y_columns. Can be hex values.
        filter_size (int, optional): size for gaussian filter.
        text_size (int, optional): Text size for the tick parameters. Defaults to 8.
        optim_text (bool, optional): automatically calculate the best text size for the tick parameters. Defaults to True.
    """

    if optim_text:
        size = fig.get_size_inches()*fig.dpi
        text_size = size[0]/100

    x = df[x_column].values
    if isinstance(y_column, str):
        y = [df[y].values for y in y_column]
    else:
        y = [df[y].values for y in y_column]

    x_smoothed = np.arange(1, len(x)+1)
    y_smoothed = [gaussian_smooth(x_smoothed, y_, filter_size) for y_ in y]

    if not colors:
        ax.stackplot(x, y_smoothed)
    else:
        ax.stackplot(x, y_smoothed, colors=colors)

    ax.legend(y_column, prop={'size': text_size})

