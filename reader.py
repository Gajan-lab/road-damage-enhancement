import cv2
import os

def read_images():

    folder_path = "frames"

    images = []

    for file in sorted(os.listdir(folder_path)):

        file_path = os.path.join(folder_path, file)

        img = cv2.imread(file_path)

        if img is not None:
            images.append((file, img))

    return images


if __name__ == "__main__":

    images = read_images()

    print("Total images loaded:", len(images))

    for name, _ in images:
        print("Loaded:", name)