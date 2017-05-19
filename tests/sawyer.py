from .context import faces

def main():
    """Animate an image of Sawyer-the-robot's face. """

    Sawyer = faces.Face('../data/sawyer.png')

    Sawyer.blink()
    
if __name__ == '__main__':
    main()
