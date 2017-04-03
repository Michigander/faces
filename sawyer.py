import faces
from faces import animations
import numpy as np
import cv2

def main():
    """
    Use the Animator to run animations on a Face formed from a sawyer robot face image.

    """
    print '[*] building face data: '
    #face_data = np.array([['1', '2', '3', '4'], ['7', '8', '9', '10'], [ '11', '12','13', '14']])
    face_data = cv2.imread('./img/sawyer/sawyer-eyes-closed.png')
    print '[*] done.'

    print '[*] building face ...'
    face = faces.Face(face_data)
    print '[*] done.'

    print '[*] building animator ... '
    animator = faces.Animator(face_data)
    print '[*] done.'

    print '[*] running single ...'
    animator.play(animations.describe)
    print '[*] done.'

if __name__ == '__main__':
    main()
