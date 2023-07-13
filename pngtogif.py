import imageio
import cv2


def processimage_png_to_gif(filename):
    image = cv2.imread(f"uploads/{filename}")
    newfilename = f"downloads/{filename.split('.')[0]}.gif"
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    imageio.mimsave(newfilename, [image_rgb])
    return newfilename

# from PIL import Image


# def png_to_gif(input_path, output_path):
#     # Open the input image
#     image = Image.open(input_path)

#     # Convert the image to RGBA if it's not already
#     if image.mode != "RGBA":
#         image = image.convert("RGBA")

#     # Create a new GIF image
#     gif_image = Image.new("P", image.size)

#     # Convert RGBA image to palette mode with a transparent background
#     gif_image.paste(image, (0, 0), image)

#     # Save the GIF image with the desired duration for each frame
#     gif_image.save(output_path, format="GIF", transparency=0,
#                    save_all=True, append_images=[image], duration=500, loop=0)

# input_path = 'C:\\Users\\dawns\\OneDrive\\Desktop\\Confil The File Coverter\\uploads\\practice.jpg'
# output_path = 'C:\\Users\\dawns\\OneDrive\\Desktop\\Confil The File Coverter\\downloads\\practice.gif'
# png_to_gif(input_path, output_path)
