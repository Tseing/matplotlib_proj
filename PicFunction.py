import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.axisartist as axisartist
import mytools

fig = plt.figure(figsize=(10,4))
ax1 = axisartist.Subplot(fig, 121)
ax2 = axisartist.Subplot(fig, 122)
fig.add_axes(ax1)
fig.add_axes(ax2)

axes_list = [ax1, ax2]

for ax in axes_list:
    ax.axis[:].set_visible(False)
    ax.axis["x"] = ax.new_floating_axis(0,0)
    ax.axis["y"] = ax.new_floating_axis(1,0)
    ax.axis["x"].set_axisline_style("-|>", size=1.5)
    ax.axis["y"].set_axisline_style("-|>", size=1.5)
    ax.axis["x"].line.set_facecolor("black")
    ax.axis["y"].line.set_facecolor("black")

    ax.set_xticks([])
    ax.set_yticks([])


x = np.arange(-6, 6, 0.1)
y = lambda x: 1/(1+np.e**(-x))
ax1.plot(x, y(x), lw=2, c="black")
mytools.autoscale(ax1, x, y(x))

x = np.arange(-6, 6, 0.1)
y = lambda x: np.e**(-x)/(1+np.e**(-x))**2
ax2.plot(x, y(x), lw=2, c="black")
mytools.autoscale(ax2, x, y(x))

plt.savefig("./images/PicFunction.jpg", bbox_inch="tight", dpi=250)
plt.show()