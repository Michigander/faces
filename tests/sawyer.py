from .context import faces

def main():
    """
    Use the Animator to run animations on a Face formed from a sawyer robot face image.

    """
    print '[*] building face ... '
    sawyer = new faces.Face('./img/sawyer/sawyer-eyes-closed.png')
    print '[*] done.'

    print '[*] blinking eyes ... '
    sawyer.blink()
    print '[*] done.'

if __name__ == '__main__':
    main()
