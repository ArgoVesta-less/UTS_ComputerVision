import numpy as np
import imutils
import cv2

# Membaca gambar langsung
image = cv2.imread("1302067.png")

# Pastikan gambar terbaca
if image is None:
    print("❌ Gambar '1302067.png' tidak ditemukan! Pastikan file ada di folder yang sama.")
    exit()

# Tampilkan gambar asli
cv2.imshow("Original", image)

# Ambil ukuran gambar
(h, w) = image.shape[:2]
center = (w // 2, h // 2)

# Putar 45 derajat searah jarum jam
M = cv2.getRotationMatrix2D(center, 45, 1.0)
rotated_45 = cv2.warpAffine(image, M, (w, h))
cv2.imshow("Rotated 45 Degrees", rotated_45)

# Putar 180 derajat menggunakan imutils
rotated_180 = imutils.rotate(image, 180)
cv2.imshow("Rotated 180 Degrees", rotated_180)

# Tunggu tombol ditekan sebelum menutup jendela
cv2.waitKey(0)
cv2.destroyAllWindows()
