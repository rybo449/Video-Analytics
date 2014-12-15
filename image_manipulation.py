import os
import sys
import numpy as np
import scipy.ndimage as nd
from scipy.ndimage.filters import median_filter as mf
import matplotlib.pyplot as plt
prt1_img =  nd.filters.median_filter(1.0*(255 - np.array([[pix[::-1] for pix in row] for row in nd.imread(os.path.join('images','ml.jpg'))[::2,::2]])),(8,2,1)).clip(0,255).astype(np.uint8)

nrow, ncol = prt1_img.shape[:2]
xsize = float(ncol)/150
ysize = float(nrow)/150
fig, ax = plt.subplots(num = 'modified Mona Lisa',figsize = [xsize,ysize], facecolor = 'w')
#fig.canvas.set_window_title('modified Mona Lisa')
fig.subplots_adjust(0,0,1,1)
ax.axis('off')
ax.imshow(prt1_img)
#fig.canvas.draw()
plt.show()