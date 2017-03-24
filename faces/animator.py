from multiprocessing import Process

class Animator(object):
    """
    Provide convenient methods for running animations on a face.

    """

    def __init__(self, face):
        """
        Constructor

        """
        self._face = face

    def play(self, animation):
        return animation(face)

    def play_sequence(self, *sequence):
        """
        Run animations in order

        """
        for animation in sequence:
            animation(face)

    def play_series(self, *series):
        """
        Run animations in parallel

        """
        processes = []

        for animation in series:
            p = Process(target=animation)
            p.start()
            processes.append(p)

        for process in processes:
            process.join()
