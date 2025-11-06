from __future__ import print_function
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=False, default="1302067.png",
                help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])

if image is None:
    print("Error: Gambar tidak ditemukan. Pastikan file '{}' ada di folder script.".format(args["image"]))
    exit()

cv2.imshow("Original", image)

(b, g, r) = image[0, 0]
print("Pixel at (0, 0) - Red: {}, Green: {}, Blue: {}".format(r, g, b))

image[0, 0] = (0, 0, 255)
(b, g, r) = image[0, 0]
print("Pixel at (0, 0) - Red: {}, Green: {}, Blue: {}".format(r, g, b))

corner = image[0:100, 0:100]
cv2.imshow("Corner", corner)

image[0:100, 0:100] = (0, 255, 0)

cv2.imshow("Updated", image)
cv2.waitKey(0)