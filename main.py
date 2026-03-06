import cv2

from reader import read_images
from denoise import gaussian_denoise
from contrast import contrast_stretch
from sharpen_save import sharpen_image, save_image


images = read_images()

print("Processing frames...")

for name, img in images:

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    denoised = gaussian_denoise(gray)

    stretched = contrast_stretch(denoised)

    sharpened = sharpen_image(stretched)

    save_image(name, sharpened)

print("All frames processed and saved.")
