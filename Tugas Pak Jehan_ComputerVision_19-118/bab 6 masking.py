import numpy as np
import cv2

# Membaca gambar langsung
image = cv2.imread("1302067.png")

# Cek apakah file gambar ditemukan
if image is None:
    print("❌ File '1302067.png' tidak ditemukan!")
    exit()

# Tampilkan gambar asli
cv2.imshow("Original", image)

# Buat mask berbentuk persegi di tengah
mask = np.zeros(image.shape[:2], dtype="uint8")
(cX, cY) = (image.shape[1] // 2, image.shape[0] // 2)
cv2.rectangle(mask, (cX - 75, cY - 75), (cX + 75, cY + 75), 255, -1)
cv2.imshow("Mask (Rectangle)", mask)

# Terapkan mask persegi ke gambar
masked = cv2.bitwise_and(image, image, mask=mask)
cv2.imshow("Masked Image (Rectangle)", masked)

# Buat mask berbentuk lingkaran di tengah
mask = np.zeros(image.shape[:2], dtype="uint8")
cv2.circle(mask, (cX, cY), 100, 255, -1)
cv2.imshow("Mask (Circle)", mask)

# Terapkan mask lingkaran ke gambar
masked = cv2.bitwise_and(image, image, mask=mask)
cv2.imshow("Masked Image (Circle)", masked)

# Tunggu tombol ditekan dan tutup semua jendela
cv2.waitKey(0)
cv2.destroyAllWindows()
