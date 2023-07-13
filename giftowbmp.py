import os
import imageio

input_dir = "C:\\Users\\dawns\\OneDrive\\Desktop\\Confil The File Coverter\\uploads"
output_dir = "C:\\Users\\dawns\\OneDrive\\Desktop\\Confil The File Coverter\\downloads"


def processiamage_gif_to_wbmp(filename):
    for file in os.listdir(input_dir):
        if file == filename:
            input_file = os.path.join(input_dir, file)
            output_file = os.path.join(
                output_dir, '{0}.wbmp'.format(file.split('.')[-2]))
            # Read the gif file
            gif = imageio.mimread(input_file)

            # Convert the gif to a numpy array
            array = imageio.volread(input_file)

            # Write the array to a wbmp file
            imageio.imwrite(output_file, array)
            return output_file
