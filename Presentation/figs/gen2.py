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

fig = plt.figure()
ax = fig.add_subplot(111)

#x = np.arange(-0.5, 0.5, 0.01)
#plt.plot(x, 2*x, linewidth='3')
#z = np.arange(0.5, 1, 0.01)
#plt.plot(z, np.ones(z.shape), linewidth='3', color='blue')

#z = np.arange(-1, -0.5, 0.01)
#plt.plot(z, -np.ones(z.shape), linewidth='3', color='blue')

grid = True
if grid:
    nx, ny = (5, 5)
    x = np.linspace(-1, 1, nx)
    y = np.linspace(-1, 1, ny)
    xv, yv = np.meshgrid(x, y)
    plt.scatter(xv, yv)

    plt.scatter(x, np.ones(x.shape)*1.1, color='red')
    plt.scatter(np.ones(y.shape)*1.1, y, color='red')
else:
    rr = np.random.rand(25, 2)*2-1
    plt.scatter(rr[:, 0], rr[:, 1])
    plt.scatter(rr[:, 0], np.ones(rr[:, 0].shape)*1.1, color='red')
    plt.scatter(np.ones(rr[:, 1].shape)*1.1, rr[:, 1], color='red')


patch = patches.PathPatch(path, facecolor='blue', lw=1, alpha='0.2')
ax.add_patch(patch)
ax.set_xlim(-1.2,1.2)
ax.set_ylim(-1.2,1.2)
plt.savefig("highDimKernel.png",bbox_inches='tight',dpi=100)

plt.show()
