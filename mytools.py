import numpy as np

def autoscale(ax, x: list, y: list, *, xscale=0.2, yscale=0.2):
    """Auto-scale the scope of function plot in the chosen coordinate system.

    Parameters:
        ax : Axes
            The chosen coordinate system.
        x : list
            Data of function plot.
        y : list
            Data of function plot.
        xscale : float, default=0.2
            Magnification of margin between plot and edge in x-axis.
        yscale : float, default=0.2
            Magnification of margin between plot and edge in y-axis.
    Return:
        None
    """
    dx = np.max(x) - np.min(x)
    dy = np.max(y) - np.min(y)
    ax.set_xlim([np.min(x)-xscale*dx, np.max(x)+xscale*dx])
    ax.set_ylim([np.min(y)-yscale*dy, np.max(y)+yscale*dy])
