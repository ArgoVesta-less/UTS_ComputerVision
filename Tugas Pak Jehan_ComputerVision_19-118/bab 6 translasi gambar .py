import numpy as np
import cv2
import imutils

# Membaca gambar langsung tanpa argparse
image = cv2.imread("1302067.png")

# Pastikan gambar berhasil dibaca
if image is None:
    print("Gambar tidak ditemukan! Pastikan file '1302067.png' ada di folder yang sama dengan skrip ini.")
    exit()

# Tampilkan gambar asli
cv2.imshow("Original", image)

# Geser ke kanan 25 piksel dan ke bawah 50 piksel
M = np.float32([[1, 0, 25], [0, 1, 50]])
shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
cv2.imshow("Shifted Down and Right", shifted)

# Geser ke kiri 50 piksel dan ke atas 90 piksel
M = np.float32([[1, 0, -50], [0, 1, -90]])
shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
cv2.imshow("Shifted Up and Left", shifted)

# Geser ke bawah 100 piksel menggunakan imutils
shifted = imutils.translate(image, 0, 100)
cv2.imshow("Shifted Down (imutils)", shifted)

# Tunggu hingga tombol ditekan
cv2.waitKey(0)
cv2.destroyAllWindows()
