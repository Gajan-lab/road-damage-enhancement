import cv2
import os
import numpy as np

def sharpen_image(image):

    kernel = np.array([[0,-1,0],
                       [-1,5,-1],
                       [0,-1,0]])

    sharp = cv2.filter2D(image, -1, kernel)

    return sharp


def save_image(filename, image):

    output_folder = "enhanced_frames"

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    save_path = os.path.join(output_folder, filename)

    cv2.imwrite(save_path, image)
