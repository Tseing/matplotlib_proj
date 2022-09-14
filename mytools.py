import numpy as np

def autoscale(ax, x: list, y: list, *, xscale=0.2, yscale=0.2, up=None,
bottom=None, left=None, right=None):
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
    if left and right != None:
        ax.set_xlim([np.min(x)-left*dx, np.max(x)+right*dx])
    else:
        ax.set_xlim([np.min(x)-xscale*dx, np.max(x)+xscale*dx])
    if bottom and up != None:
        ax.set_ylim([np.min(y)-bottom*dy, np.max(y)+up*dy])
    else:
        ax.set_ylim([np.min(y)-yscale*dy, np.max(y)+yscale*dy])
