
import pathlib

dirpath = pathlib.Path(__file__)


def makeicon():
    import PythonMagick
    img = PythonMagick.Image(str(dirpath.parent / 'images/black_bishop.png'))
    img.sample('256x256')
    img.write(str(dirpath.parent / 'images/favicon.ico'))


def main():
    makeicon()


if __name__ == '__main__':
    main()
