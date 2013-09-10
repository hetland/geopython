
import numpy as np
import matplotlib.pyplot as plt

y, x = np.mgrid[-5:5:201j, -5:5:101j]

z = np.zeros_like(x)

for n in range(10):
    xo, yo = np.random.randn(2)
    z += np.exp( -(x-xo)**2 - (y-yo)**2)


fig = plt.figure(figsize=(6,8))
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
pc = ax.pcolor(x, y, z, cmap=plt.cm.Reds)

cb = plt.colorbar(pc, orientation='horizontal')
cb.set_label(r'Energy [m$^3$ s$^{-2}$]')

ax.set_aspect(1.0)
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)

ax.set_xlabel('Distance [km]')
ax.set_ylabel('Distance [km]')
ax.set_title('One plot to rule them all')

plt.show()