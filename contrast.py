import numpy as np

def contrast_stretch(image):

    min_val = image.min()
    max_val = image.max()

    if max_val == min_val:
        return image

    dmin = 50
    dmax = 200

    stretched = dmin + (image - min_val) * ((dmax - dmin)/(max_val - min_val))

    return stretched.astype("uint8")
