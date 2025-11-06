import numpy as np
import cv2

# Membaca gambar langsung
image = cv2.imread("1302067.png")

# Pastikan gambar berhasil dibaca
if image is None:
    print("❌ File '1302067.png' tidak ditemukan! Pastikan file ada di folder yang sama.")
    exit()

# Tampilkan gambar asli
cv2.imshow("Original", image)

# Contoh operasi add dan subtract pada array kecil
print("max of 255:", cv2.add(np.uint8([200]), np.uint8([100])))  # hasilnya 255, bukan 300 (karena batas maksimum 255)
print("min of 0:", cv2.subtract(np.uint8([50]), np.uint8([100])))  # hasilnya 0, bukan -50 (karena batas minimum 0)

# Tambahkan nilai kecerahan (brightness)
M = np.ones(image.shape, dtype="uint8") * 100
added = cv2.add(image, M)
cv2.imshow("Added (lebih cerah)", added)

# Kurangi nilai kecerahan
M = np.ones(image.shape, dtype="uint8") * 50
subtracted = cv2.subtract(image, M)
cv2.imshow("Subtracted (lebih gelap)", subtracted)

# Tunggu tombol ditekan, lalu tutup semua jendela
cv2.waitKey(0)
cv2.destroyAllWindows()
