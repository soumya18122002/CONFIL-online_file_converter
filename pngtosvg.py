import os
from PIL import Image
import svgwrite


def png_to_svg(png_file_path, svg_file_path):
    # Open the PNG file
    with Image.open(png_file_path) as png_image:
        # Create a new SVG file
        with open(svg_file_path, 'w') as svg_file:
            # Create an SVG drawing object
            drawing = svgwrite.Drawing(svg_file.name, size=png_image.size)
            # Add an image element to the drawing
            drawing.add(svgwrite.image.Image(
                href=png_file_path, size=png_image.size))
            # Save the drawing as an SVG file
            drawing.save()


def processimage_png_to_svg(filename):
    input_dir = 'C:\\Users\\dawns\\OneDrive\\Desktop\\Confil The File Coverter\\uploads'
    output_dir = 'C:\\Users\\dawns\\OneDrive\\Desktop\\Confil The File Coverter\\downloads'
    for file in os.listdir(input_dir):
        if file == filename:
            source_path = os.path.join(input_dir, file)
            output_path = os.path.join(
                output_dir, '{0}.svg'.format(file.split('.')[-2]))
            png_to_svg(source_path, output_path)
            return output_path
