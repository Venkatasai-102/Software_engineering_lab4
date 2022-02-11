#Imports
import numpy as np
from PIL import Image

class CropImage(object):
    '''
        Performs either random cropping or center cropping.
    '''
    def __init__(self, shape, crop_type='center'):
        '''
            Arguments:
            shape: output shape of the crop (h, w)
            crop_type: center crop or random crop. Default: center
        '''

        # Write your code here
        self.shp = shape
        self.crp_tp = crop_type

    def __call__(self, image): # Assuming the sample is given as PIL image format
        '''
            Arguments:
            image (numpy array or PIL image)

            Returns:
            image (numpy array or PIL image)
        '''

        # Write your code here
        nparr = np.zeros((1,1)) # a numpy array to check the type of the image

        
        if type(image) != type(nparr): # If sample is in the PIL image format
            image = np.asarray(image)

        hgt, wdt, oth = image.shape

        h, w = self.shp

        if h > hgt:
            h = hgt
        if w > wdt:
            w = wdt
        
        # self.shp = (h, w)

        if self.crp_tp == "random":
            strt_h = np.random.randint(0, hgt - h)
            strt_w = np.random.randint(0, wdt - w)
        else:
            strt_h = (hgt-h)//2
            strt_w = (wdt-w)//2
        
        image = image[strt_h: strt_h+h, strt_w: strt_w+w] # cropping the image

        # return image # If we want to return the image as numpy array
        return Image.fromarray(image) # returning the image as PIL image format