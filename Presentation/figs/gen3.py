import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches
import numpy as np
verts = [
    (-1., -1.), # left, bottom
    (-1., 1.), # left, top
    (1., 1.), # right, top
    (1., -1.), # right, bottom
    (0., 0.), # ignored
    ]

codes = [Path.MOVETO,
         Path.LINETO,
         Path.LINETO,
         Path.LINETO,
         Path.CLOSEPOLY,
         ]

path = Path(verts, codes)

fig = plt.figure(facecolor='white')
ax = fig.add_subplot(111, aspect='equal')
ax.set_frame_on(False)
ax.axes.get_yaxis().set_visible(False)
ax.axes.get_xaxis().set_visible(False)

plt.arrow( -2.05, 0, 0.7, 0, fc="k", ec="k",
head_width=0.5, head_length=0.2, linewidth='2')

plt.arrow( 1.2, 0, 0.7, 0, fc="k", ec="k",
head_width=0.5, head_length=0.2, linewidth='2')

plt.text(-2.5, -0.1, r'$x$', fontsize=30)

plt.text(2.3, -0.1, r'$f(x) + \epsilon$', fontsize=30)

plt.text(-0.95, -0.1, r'Black Box', fontsize=27, color='white')

patch = patches.PathPatch(path, facecolor='black', lw=1, alpha='1')
ax.add_patch(patch)
ax.set_xlim(-2.6, 4)
ax.set_ylim(-1.2,1.2)
plt.savefig("highDimKernel.pdf",bbox_inches='tight',dpi=100)

plt.show()
