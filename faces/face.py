import numpy as np
import matplotlib.pyplot as plt
from skimage import measure, io, color

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

    def get_description(self):
        """ Return statistics about face. """

        return {
            "shape" : self._face_array.shape,
            "size" : self._face_array.size,
            "dtype" : self._face_array.dtype
        }

    def get_contours(self):
        """ Provides the contours of the face. """

        return self._contours

    def generate_contours(self):
        """ Generates the contours for current face """

        # reduce dimenstion
        face_grayscale = color.rgb2gray(self._face_array)

        # find contours
        return measure.find_contours(face_grayscale, 0.8)


    def show_contours(self):
        """ Show face in a window """

        # configure 
        fig, ax = plt.subplots()

        # show
        ax.imshow(self._face_array, interpolation='nearest', cmap=plt.cm.gray)

        # plot
        for n, contour in enumerate(self._contours):
            print('contour #', n, ' -> ', contour)
            ax.plot(contour[:,1], contour[:,0], linewidth=2)

        ax.axis('image')
        ax.set_xticks([])
        ax.set_yticks([])

        plt.show()
