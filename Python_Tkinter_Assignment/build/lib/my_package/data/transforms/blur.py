#Imports
from PIL import ImageFilter, Image
import numpy as np # if working with numpy arrays

class BlurImage(object):
    '''
        Applies Gaussian Blur on the image.
    '''

    def __init__(self, radius):
        '''
            Arguments:
            radius (int): radius to blur
        '''

        # Write your code here
        self.gsian_radius = radius # assigning the value of radius to the object to be blurred
        

    def __call__(self, image): # Assuming the sample is given as PIL image format
        '''
            Arguments:
            image (numpy array or PIL Image)

            Returns:
            image (numpy array or PIL Image)
        '''

        # Write your code here
        nparr = np.zeros((1,1)) # a numpy array to check the type of the image

        if type(image) == type(nparr):
            image = Image.fromarray(image)
        
        image = image.filter(ImageFilter.GaussianBlur(self.gsian_radius)) # Blurring the image
        # return np.asarray(image) # If we want to return the image as numpy array
        return image # returning the image as PIL image format