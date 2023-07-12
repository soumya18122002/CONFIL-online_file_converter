import os
from PIL import Image
source_dir = 'C:\\Users\\dawns\\OneDrive\\Desktop\\Confil The File Coverter\\uploads'
output_dir = 'C:\\Users\\dawns\\OneDrive\\Desktop\\Confil The File Coverter\\downloads'


def processimage_jpg_to_pdf(filename):
    for file in os.listdir(source_dir):
        if file == filename:
            img = Image.open(os.path.join(source_dir, file))
            im_con = img.convert('RGB')
            im_con.save(os.path.join(
                output_dir, '{0}.pdf'.format(file.split('.')[-2])))
            x = os.path.join(
                output_dir, '{0}.pdf'.format(file.split('.')[-2]))
            return x
