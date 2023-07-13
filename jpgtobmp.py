import cv2


def processimage_jpg_to_bmp(filename):
    img = cv2.imread(f"uploads/{filename}")
    newfilename = f"downloads/{filename.split('.')[0]}.bmp"
    cv2.imwrite(newfilename, img)
    return newfilename

