import faces
import numpy as np

def main():
    """
    Use the Animator to run animations on a Face formed from a sawyer robot face image.

    """

    print '[*] printing face data: '
    face_data = [['1', '2', '3', '4'], ['7', '8', '9', '10'], [ '11', '12','13', '14']]
    print '[*] done.'

    print '[*] building face ...'
    face = faces.Face(face_data)
    print '[*] done.'

    print '[*] building animator ... '
    animator = faces.Animator(face_data)
    print '[*] done.'

    print '[*] running single ...'
    animator.play(some_animation)
    print '[*] done.'

def some_animation(face):
    print '[!] running some_animation on '
    print face

if __name__ == '__main__':
    main()
