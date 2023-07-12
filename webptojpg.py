import cv2
def processimage_webp_to_jpg(filename):
    img = cv2.imread(f"uploads/{filename}")
    newfilename = f"downloads/{filename.split('.')[0]}.jpg"
    cv2.imwrite(newfilename,img)
    return newfilename
