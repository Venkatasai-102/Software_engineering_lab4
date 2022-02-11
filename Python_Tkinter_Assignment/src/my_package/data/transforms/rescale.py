#Imports
import cv2
import numpy as np
from PIL import Image

class RescaleImage(object):
    '''
        Rescales the image to a given size.
    '''


    def __init__(self, output_size):
        '''
            Arguments:
            output_size (tuple or int): Desired output size. If tuple, output is
            matched to output_size. If int, smaller of image edges is matched
            to output_size keeping aspect ratio the same.
        '''

        # Write your code here
        self.obj_sz = output_size

    def __call__(self, image):
        '''
            Arguments:
            image (numpy array or PIL image)

            Returns:
            image (numpy array or PIL image)

            Note: You do not need to resize the bounding boxes. ONLY RESIZE THE IMAGE.
        '''

        # Write your code here
        nparr = np.zeros((1,1)) # a numpy array to check the type of the image

        if type(image) != type(nparr): # If sample is in the PIL image format
            image = np.asarray(image)

        var = int(1) # Variable to check if initialized output size is integer type or not
        h, w, o = image.shape

        if type(self.obj_sz) == type(var):
            if h > w:
                asp_rt = h/w
                new_w = self.obj_sz
                new_h = (self.obj_sz)*asp_rt*new_w
                self.obj_sz = (new_h, new_w)
            else:
                asp_rt = w/h
                new_h = self.obj_sz
                new_w = (self.obj_sz)*asp_rt*new_h
                self.obj_sz = (new_h, new_w)

        image = cv2.resize(image, self.obj_sz, interpolation= cv2.INTER_LINEAR)
        # return image # If we want to return the image as numpy array
        return Image.fromarray(image) # returning the image as PIL image format