import numpy as np
import cv2

# Membaca gambar langsung
image = cv2.imread("1302067.png")

# Pastikan gambar ditemukan
if image is None:
    print("❌ File '1302067.png' tidak ditemukan! Pastikan file ada di folder yang sama.")
    exit()

# Tampilkan gambar asli
cv2.imshow("Original", image)

# Crop area tertentu dari gambar (y: 30–120, x: 240–335)
cropped = image[30:120, 240:335]

# Tampilkan hasil crop
cv2.imshow("Cropped Region", cropped)

# Tunggu tombol ditekan lalu tutup semua jendela
cv2.waitKey(0)
cv2.destroyAllWindows()
