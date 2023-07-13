import cv2


def processimage_png_to_tiff(filename):
    img = cv2.imread(f"uploads/{filename}")
    newfilename = f"downloads/{filename.split('.')[0]}.tiff"
    cv2.imwrite(newfilename, img)
    return newfilename
