import numpy as np
import matplotlib.pyplot as plt
from skimage import measure, io, color

import engine
import brain

class Face:
    """ Represent the face as an array of pixels from an image. """

    def __init__(self, filepath):
        """ Constructor """

        # set face path
        self._path = filepath

        # image -> matrix
        self._matrix = io.imread(self._path)

        # set components
        self._features = engine.generate_features(self._contours)

    def describe(self):
        """ Return statistics about face. """

        return {
            "shape" : self._matrix.shape,
            "size" : self._matrix.size,
            "dtype" : self._matrix.dtype
        }
