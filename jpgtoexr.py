import os
import OpenEXR
import Imath
import PIL.Image
import numpy as np

input_dir = 'C:\\Users\\dawns\\OneDrive\\Desktop\\Confil The File Coverter\\uploads'
output_dir = 'C:\\Users\\dawns\\OneDrive\\Desktop\\Confil The File Coverter\\downloads'


def processimage_jpg_to_exr(filename):
    for file in os.listdir(input_dir):
        if file == filename:
            input_file = os.path.join(input_dir, file)
            output_file = os.path.join(
                output_dir, '{0}.exr'.format(file.split('.')[-2]))

            # Read the jpg file
            jpg = PIL.Image.open(input_file)
            array = np.array(jpg)

            header = OpenEXR.Header(array.shape[1], array.shape[0])
            data = {'R': array[:, :, 0].astype(np.float32).tobytes(), 'G': array[:, :, 1].astype(
                np.float32).tobytes(), 'B': array[:, :, 2].astype(np.float32).tobytes()}

            # Transpose the data for each channel
            data['R'] = data['R'][::-1]
            data['G'] = data['G'][::-1]
            data['B'] = data['B'][::-1]

            # Write the header and data to an exr file
            exr = OpenEXR.OutputFile(output_file, header)
            exr.writePixels(data)
            exr.close()
            return output_file
