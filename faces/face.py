import numpy as np
from scipy import misc, ndimage

class Face(object):
    """
    Represent the face as an array of pixels from an image.

    """

    def __init__(self, filepath):
        """
        Constructor

        """

        # read image as numpy array
        self._face_array = misc.imread(filepath)

    def get_data(self):
        """
        Return the face array.

        """
        return self._face_array

    def about():
        """
        Return statistics about face.

        """
        return {
            "shape" : self._face_array.shape,
            "size" : self._face_array.size,
            "dtype" : self._face_array.dtype
        }
