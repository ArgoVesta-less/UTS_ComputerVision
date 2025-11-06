import numpy as np
import cv2

# Baca gambar langsung tanpa argparse
image = cv2.imread("1302067.png")
cv2.imshow("Original", image)

# === 1. Average Blurring ===
blurred = np.hstack([
    cv2.blur(image, (3, 3)),
    cv2.blur(image, (5, 5)),
    cv2.blur(image, (7, 7))
])
cv2.imshow("Average Blurring", blurred)
cv2.waitKey(0)

# === 2. Gaussian Blurring ===
blurred = np.hstack([
    cv2.GaussianBlur(image, (3, 3), 0),
    cv2.GaussianBlur(image, (5, 5), 0),
    cv2.GaussianBlur(image, (7, 7), 0)
])
cv2.imshow("Gaussian Blurring", blurred)
cv2.waitKey(0)

# === 3. Median Blurring ===
blurred = np.hstack([
    cv2.medianBlur(image, 3),
    cv2.medianBlur(image, 5),
    cv2.medianBlur(image, 7)
])
cv2.imshow("Median Blurring", blurred)
cv2.waitKey(0)

# === 4. Bilateral Filtering ===
blurred = np.hstack([
    cv2.bilateralFilter(image, 5, 21, 21),
    cv2.bilateralFilter(image, 7, 31, 31),
    cv2.bilateralFilter(image, 9, 41, 41)
])
cv2.imshow("Bilateral Filtering", blurred)
cv2.waitKey(0)

cv2.destroyAllWindows()
