import numpy as np
import cv2

# Membaca gambar
image = cv2.imread("1302067.png")

if image is None:
    print("❌ File '1302067.png' tidak ditemukan!")
    exit()

cv2.imshow("Original", image)

# Membuat mask lingkaran di tengah gambar
mask = np.zeros(image.shape[:2], dtype="uint8")
(cX, cY) = (image.shape[1] // 2, image.shape[0] // 2)
cv2.circle(mask, (cX, cY), 100, 255, -1)
cv2.imshow("Mask (Circle)", mask)

# Operasi bitwise
masked_and = cv2.bitwise_and(image, image, mask=mask)
cv2.imshow("Bitwise AND (masked)", masked_and)

bitwise_not = cv2.bitwise_not(image)
cv2.imshow("Bitwise NOT (invers warna)", bitwise_not)

cv2.waitKey(0)
cv2.destroyAllWindows()
