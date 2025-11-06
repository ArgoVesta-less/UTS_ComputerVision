import numpy as np
import cv2

# Membaca gambar langsung dari file
image = cv2.imread("1302067.png")

# Cek apakah gambar berhasil dibaca
if image is None:
    print("❌ File '1302067.png' tidak ditemukan! Pastikan file ada di folder yang sama dengan script ini.")
    exit()

# Tampilkan gambar asli
cv2.imshow("Original", image)

# Konversi ke Grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray", gray)

# Konversi ke HSV
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
cv2.imshow("HSV", hsv)

# Konversi ke LAB
lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
cv2.imshow("L*a*b*", lab)

# Tunggu hingga tombol ditekan, lalu tutup semua jendela
cv2.waitKey(0)
cv2.destroyAllWindows()
