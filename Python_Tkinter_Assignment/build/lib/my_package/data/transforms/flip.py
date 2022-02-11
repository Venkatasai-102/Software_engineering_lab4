#Imports
from PIL import Image
import numpy as np # if working with numpy arrays


class FlipImage(object):
    '''
        Flips the image.
    '''

    def __init__(self, flip_type='horizontal'):
        '''
            Arguments:
            flip_type: 'horizontal' or 'vertical' Default: 'horizontal'
        '''

        # Write your code here
        self.flp_type = flip_type # Assigning the value of flip type to the class variable

        
    def __call__(self, image): # Assuming the sample is given as PIL image format
        '''
            Arguments:
            image (numpy array or PIL image)

            Returns:
            image (numpy array or PIL image)
        '''

        # Write your code here
        nparr = np.zeros((1,1)) # a numpy array to check the type of the image

        if type(image) == type(nparr): # If sample is in the numpy array format
            image = Image.fromarray(image)

        if self.flp_type == 'horizontal':
            image =  image.transpose(Image.FLIP_LEFT_RIGHT) # flipping the image
        else:
            image =  image.transpose(Image.FLIP_TOP_BOTTOM) # flipping the image
        
        # return np.asarray(image) # If we want to return the image as numpy array
        return image # returning the image as PIL image format