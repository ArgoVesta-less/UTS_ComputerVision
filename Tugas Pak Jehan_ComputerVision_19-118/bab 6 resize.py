import numpy as np
import imutils
import cv2

# Membaca gambar langsung
image = cv2.imread("1302067.png")

# Pastikan gambar ditemukan
if image is None:
    print("❌ File '1302067.png' tidak ditemukan! Pastikan file ada di folder yang sama.")
    exit()

# Tampilkan gambar asli
cv2.imshow("Original", image)

# Resize berdasarkan lebar (width = 150px)
r = 150.0 / image.shape[1]
dim = (150, int(image.shape[0] * r))
resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
cv2.imshow("Resized (Width 150px)", resized)

# Resize berdasarkan tinggi (height = 50px)
r = 50.0 / image.shape[0]
dim = (int(image.shape[1] * r), 50)
resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
cv2.imshow("Resized (Height 50px)", resized)

# Resize menggunakan imutils (width = 100px)
resized = imutils.resize(image, width=100)
cv2.imshow("Resized via imutils", resized)

# Tunggu tombol ditekan, lalu tutup semua jendela
cv2.waitKey(0)
cv2.destroyAllWindows()
