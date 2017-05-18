from face import Face

def main():
    """ Run demo. """

    # build face
    sawyer = Face('./data/sawyer/sawyer-eyes-closed.png')

    # facial features
    features = sawyer.get_features()

if __name__ == '__main__':
    main()
