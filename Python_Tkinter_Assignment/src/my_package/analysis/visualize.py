#Imports
from PIL import Image, ImageDraw
import numpy as np

def plot_visualization(image, bboxes, classes, masks): # Write the required arguments

	# The function should plot the predicted segmentation maps and the bounding boxes on the images and save them.
	# Tip: keep the dimensions of the output image less than 800 to avoid RAM crashes.
	image_orgnl = Image.fromarray(np.uint8(image)).convert("RGB")
	image_orgn2 = Image.fromarray(np.uint8(image)).convert("RGB")
	
	for i, crd in enumerate(bboxes):
		if i >= 3:
			break

		shp = [(crd[0][0], crd[0][1]), (crd[1][0], crd[1][1])]

		img1 = ImageDraw.Draw(image_orgn2)
		img1.text((crd[0][0]+10, crd[0][1]-10), classes[i], fill="red")
		img1.rectangle(shp, outline ="red") # makinbg a border box

	for i, crd in enumerate(bboxes):
		if i >= 3:
			break

		msk = masks[i]*255 # 1, h, w
		msk = np.transpose(msk, (1, 2, 0)) # h, w, 1

		h, w, o = msk.shape
		msk = np.reshape(msk, (h, w))
		img_msk = Image.fromarray(np.uint8(msk))
		
		rnd_clr = tuple(np.random.choice(range(256), size=3)) # making a random color

		img_msk = img_msk.convert("RGB")

		# making the mask transparent i.e., same as original image at pixel which are black to remove the dimness after applying mask and 
		# applying a color randomly where the segmentation is there
		for ht in range(h):
			for wd in range(w):
				px1 = image_orgnl.getpixel((wd, ht))
				px2 = img_msk.getpixel((wd, ht))

				if px2[0] < 85 and px2[1] < 85 and px2[2] < 85:
					img_msk.putpixel((wd, ht), px1) # putting the color of orignal image
				else:
					img_msk.putpixel((wd, ht), rnd_clr) # putting random color generated
					
		image_orgnl = Image.blend(image_orgnl, img_msk, 0.4) # blending one image over other

	return image_orgnl, image_orgn2
	