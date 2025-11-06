import numpy as np
import cv2

# Membaca gambar langsung
image = cv2.imread("1302067.png")

# Cek apakah gambar ditemukan
if image is None:
    print("❌ File '1302067.png' tidak ditemukan!")
    exit()

# Tampilkan gambar asli
cv2.imshow("Original", image)

# Pisahkan channel warna (B, G, R)
(B, G, R) = cv2.split(image)

# Tampilkan tiap channel
cv2.imshow("Red", R)
cv2.imshow("Green", G)
cv2.imshow("Blue", B)

# Gabungkan kembali channel warna
merged = cv2.merge([B, G, R])
cv2.imshow("Merged", merged)

# Buat layer hitam untuk menampilkan tiap channel secara terpisah
zeros = np.zeros(image.shape[:2], dtype="uint8")

# Tampilkan channel merah, hijau, dan biru secara individual dengan warna aslinya
cv2.imshow("Red Channel", cv2.merge([zeros, zeros, R]))
cv2.imshow("Green Channel", cv2.merge([zeros, G, zeros]))
cv2.imshow("Blue Channel", cv2.merge([B, zeros, zeros]))

# Tunggu tombol ditekan, lalu tutup semua jendela
cv2.waitKey(0)
cv2.destroyAllWindows()
