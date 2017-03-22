import numpy as np

class Face(object):
    """
    Represent the face as an array of pixels from an image.

    """

    def __init__(self, filename):
        """
        Constructor

        """

        self._face_array = np.fromfile(filename)

    def get_face_array(self):
        """
        Return the current face.

        """
        return self._face_array
