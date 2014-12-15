import os
import sys
import scipy.ndimage as nd
import matplotlib.pyplot as plt

plt.ion()



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

plt.show()

while True:


		pnts = fig0.ginput(2)

		x0, y0 = int(round(pnts[0][0])), int(round(pnts[0][1]))

		x1, y1 = int(round(pnts[1][0])), int(round(pnts[1][1]))

		if x0 == x1 and y0 == y1:

			for i in range(3):

				ax1[i].cla()

			for i in range(3):
			
				ax1[i].hist(img_ml[:,:,i].flatten(), bins = 256, range = (0,255), color=colors[i], normed=True)
				ax1[i].set_ylim(0,.05)
			
			fig1.canvas.draw()


		elif x0 <= x1 and y0 <= y1:

			stamp = img_ml[x0:x1,y0:y1]

			for i in range(3):

				ax1[i].cla()

			for i in range(3):
			
				ax1[i].set_xlim(0,256)

				ax1[i].set_ylim(0,.05)
			
				ax1[i].hist(stamp[:,:,i].flatten(), bins = 256, range = (0,255), color=colors[i], normed=True)
			

			fig1.canvas.draw()

		else:

			break

		fig1.show()
