# image_exploration_part2




#


import os

import sys

import numpy as np

import scipy.ndimage as nd

import matplotlib.pyplot as plt



#


#plt.ion()



#


dpath = sys.argv[1]

fname = sys.argv[2]

infile = os.path.join(dpath,fname)

img_ml = nd.imread(infile)


nrow, ncol = img_ml.shape[:2]

xsize = float(ncol)/125

ysize = float(nrow)/125

fig0, ax0 = plt.subplots(figsize = [xsize,ysize])

fig0.subplots_adjust(0,0,1,1)

ax0.axis('off')

fig0.canvas.set_window_title(str(fname))

img0 = ax0.imshow(img_ml)

fig0.canvas.draw()



fig1, ax1 = plt.subplots(3,1, figsize = [2*xsize,ysize])

colors = ['r', 'g', 'b']

for i in range(3):

    ax1[i].hist(img_ml[:,:,i].flatten(), bins = 256, range = (0,255), normed=True, color=colors[i])
    
    ax1[i].set_ylim(0,.05)
    
    ax1[i].set_xlim(0,256)


fig1.canvas.draw()

firstTime = True

while True:

    pts = fig1.ginput(3)

    x0 = int(round(pts[0][0]))

    x1 = int(round(pts[1][0]))

    x2 = int(round(pts[2][0]))

    if firstTime:

    	rng0 = ax1[0].axvspan(x0+5, x0-5, facecolor = 'lime', alpha = .1)
    	
    	rng1 = ax1[1].axvspan(x1+5, x1-5, facecolor = 'lime', alpha = .1)
    	
    	rng2 = ax1[2].axvspan(x2+5, x2-5, facecolor = 'lime', alpha = .1)

    else:

    	
    	spn0 = rng0.get_xy()
    	
    	spn0[:,0] = [x0-5,x0-5,x0+5,x0+5,x0-5]
    	
    	rng0.set_xy(spn0)


    	spn1 = rng1.get_xy()
    	
    	spn1[:,0] = [x1-5,x1-5,x1+5,x1+5,x1-5]
    	
    	rng1.set_xy(spn1)


    	spn2 = rng2.get_xy()
    	
    	spn2[:,0] = [x2-5,x2-5,x2+5,x2+5,x2-5]
    	
    	rng2.set_xy(spn2)

    fig1.canvas.draw()

    firstTime = False

    img_copy = img_ml.copy()
    
    pixVal = [x0, x1, x2]

    for i in range(3):
        
        img_copy[:,:,i][(img_copy[:,:,i] > (pixVal[i] + 5)) | (img_copy[:,:,i] < (pixVal[i] - 5))] = img_copy[:,:,i][(img_copy[:,:,i] > (pixVal[i] + 5)) | (img_copy[:,:,i] < (pixVal[i] - 5))] * .25

    img0.set_data(img_copy.clip(0,255).astype(np.uint8))
    
    fig0.canvas.draw()

    fig0.show()