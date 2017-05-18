import numpy as np
import matplotlib.pyplot as plt
from skimage import measure, io, color

import engine

class Face:
    """ Represent the face as an array of pixels from an image. """

    def __init__(self, filepath):
        """ Constructor """

        # set face path
        self._path = filepath

        # load face array
        self._face_array = io.imread(self._path)

        # set contours
        self._contours = generate_contours(self._face_array)

        # set components
        self._features = generate_features(self._contours)

    def describe(self):
        """ Return statistics about face. """

        return {
            "shape" : self._face_array.shape,
            "size" : self._face_array.size,
            "dtype" : self._face_array.dtype
        }
