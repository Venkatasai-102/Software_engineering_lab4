#Imports
from PIL import Image
import numpy as np

class RotateImage(object):
    '''
        Rotates the image about the centre of the image.
    '''

    def __init__(self, degrees):
        '''
            Arguments:
            degrees: rotation degree.
        '''
        
        # Write your code here
        self.rte_deg = degrees # assigning the degrees to be rotated to the object

    def __call__(self, sample):
        '''
            Arguments:
            image (numpy array or PIL image)

            Returns:
            image (numpy array or PIL image)
        '''

        # Write your code here
        nparr = np.zeros((1,1)) # a numpy array to check the type of the image

        if type(sample) == type(nparr): # If sample is in the numpy array format
            sample = Image.fromarray(sample)

        sample = sample.rotate(self.rte_deg, expand=1) # rotating the image
        
        # return np.asarray(sample) # If we want to return the image as numpy array
        return sample # returning the image as PIL image format