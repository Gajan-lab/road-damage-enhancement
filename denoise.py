import cv2

def gaussian_denoise(image):

    smooth = cv2.GaussianBlur(image, (5,5), 0)

    return smooth
