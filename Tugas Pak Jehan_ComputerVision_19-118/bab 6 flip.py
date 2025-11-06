import cv2

# Membaca gambar langsung dari file
image = cv2.imread("1302067.png")

# Pastikan gambar berhasil dibaca
if image is None:
    print("❌ File '1302067.png' tidak ditemukan! Pastikan file ada di folder yang sama.")
    exit()

# Tampilkan gambar asli
cv2.imshow("Original", image)

# Flip horizontal (kanan <-> kiri)
flipped = cv2.flip(image, 1)
cv2.imshow("Flipped Horizontally", flipped)

# Flip vertikal (atas <-> bawah)
flipped = cv2.flip(image, 0)
cv2.imshow("Flipped Vertically", flipped)

# Flip dua arah (atas-bawah dan kanan-kiri)
flipped = cv2.flip(image, -1)
cv2.imshow("Flipped Both", flipped)

# Tunggu tombol ditekan, lalu tutup semua jendela
cv2.waitKey(0)
cv2.destroyAllWindows()
