import os
from PIL import Image

source_file = 'C:\\Users\\dawns\\OneDrive\\Desktop\\Confil The File Coverter\\uploads'
output_file = 'C:\\Users\\dawns\\OneDrive\\Desktop\\Confil The File Coverter\\downloads'


def processimage_png_to_ico(filename):
    for file in os.listdir(source_file):
        if file == filename:
            image = Image.open(os.path.join(source_file, file))
            x = os.path.join(
                output_file, '{0}.ico'.format(file.split('.')[-2]))
            image.save(x, format='ICO')
            return x
