import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.axisartist as axisartist
import mytools
import myconfig

fig = plt.figure(figsize=(14,4))
ax1 = axisartist.Subplot(fig, 131)
ax2 = axisartist.Subplot(fig, 132)
ax3 = axisartist.Subplot(fig, 133)
fig.add_axes(ax1)
fig.add_axes(ax2)
fig.add_axes(ax3)

axes_list = [ax1, ax2, ax3]

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

def convex_func(x):
    return x**2 - 6*x + 10

x = np.arange(1, 5.1, 0.1)
for ax in axes_list:
    ax.plot(x, convex_func(x), lw=2, c="black")
    mytools.autoscale(ax, x, convex_func(x), xscale=0.4, bottom=0.4, up=0.2)
    ax.plot([3, 3],[0, convex_func(3)], c="black", ls="--")


ax1.plot([1.2, 1.2],[0, convex_func(1.2)], c="black", ls="--")
ax1.plot([2, 2],[0, convex_func(2)], c="black", ls="--")
ax1.annotate(r"$L$", [1,-0.6], fontsize=17)
ax1.annotate(r"$H$", [1.8,-0.6], fontsize=17, c='red')
ax1.annotate(r"$\alpha^{\mathrm{new,unc}}$", [2.8,-0.6], fontsize=17)
x_fill = np.arange(1.2, 2, 0.05)
ax1.fill_between(x_fill, convex_func(x_fill), fc="white", hatch="//")

ax2.plot([2, 2],[0, convex_func(2)], c="black", ls="--")
ax2.plot([4, 4],[0, convex_func(4)], c="black", ls="--")
ax2.annotate(r"$L$", [1.8,-0.6], fontsize=17)
ax2.annotate(r"$H$", [4.3,-0.6], fontsize=17)
ax2.annotate(r"$\alpha^{\mathrm{new,unc}}$", [2.3,-0.6], fontsize=17, c='red')
x_fill = np.arange(2, 4, 0.05)
ax2.fill_between(x_fill, convex_func(x_fill), fc="white", hatch="//")

ax3.plot([4, 4],[0, convex_func(4)], c="black", ls="--")
ax3.plot([4.8, 4.8],[0, convex_func(4.8)], c="black", ls="--")
ax3.annotate(r"$L$", [3.8,-0.6], fontsize=17, c='red')
ax3.annotate(r"$H$", [4.6,-0.6], fontsize=17)
ax3.annotate(r"$\alpha^{\mathrm{new,unc}}$", [1.8,-0.6], fontsize=17)
x_fill = np.arange(4, 4.8, 0.05)
ax3.fill_between(x_fill, convex_func(x_fill), fc="white", hatch="//")

ax1.annotate(r"$\alpha^{\mathrm{new}}=H$", [2, 5.5], fontsize=17)
ax2.annotate(r"$\alpha^{\mathrm{new}}=\alpha^{\mathrm{new,unc}}$", [1.7, 5.5], fontsize=17)
ax3.annotate(r"$\alpha^{\mathrm{new}}=L$", [2, 5.5], fontsize=17)

plt.savefig("./images/220914.jpg", bbox_inch="tight", dpi=250)
plt.show()