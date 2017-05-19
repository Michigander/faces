"""engine.
+ generates the face
+ generates the nervous system
+ handles sensory i/o

"""
def generate_contours(self):
    """Generates the contours for current face """

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
class Animation(object):
    """
    The extensible base class for a face animation.

    """
    def __init__(self):
        """ Construct Animation """

        self._mask = mask

    def play():
        """ Play an animation. """


class Wink(Animation):
    """ A simple animation.

    """
    def __init__(self, face):
        """ Construct Wink Animation """

        super(Wink,self).__init__()

class Match(Animation):
    """ Animation using inpainting to match a particular expression """

    def __init__(self):
        """ Construct """"

class Animator(object):
    """ Provide convenient methods for running animations on a face. """

    def __init__(self, face):
        """ Construct animator of a particular face """

        self._face = face

    def play(self, animation):
        """ Run a single animation """

        return animation(self._face)

    def play_sequence(self, *sequence):
        """ Run animations in order """

        for animation in sequence:
            animation(self._face)

    def play_series(self, *series):
        """ Run animations in parallel """

        processes = []

        for animation in series:
            p = Process(target=animation)
            p.start()
            processes.append(p)

        for process in processes:
            process.join()
