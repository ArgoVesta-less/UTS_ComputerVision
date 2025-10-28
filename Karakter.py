import cv2
import numpy as np

# Buat kanvas hitam ukuran 400x400 piksel
canvas = np.zeros((400, 400, 3), dtype=np.uint8)

# Warna putih untuk stickman (BGR)
white = (0, 255, 255)

# Kepala (circle)
cv2.circle(canvas, (200, 100), 30, white, 2)

# Badan (line)
cv2.line(canvas, (200, 130), (200, 250), white, 2)

# Tangan kiri dan kanan
cv2.line(canvas, (200, 160), (150, 200), white, 2)
cv2.line(canvas, (200, 160), (250, 200), white, 2)

# Kaki kiri dan kanan
cv2.line(canvas, (200, 250), (160, 320), white, 2)
cv2.line(canvas, (200, 250), (240, 320), white, 2)

# Teks nama
cv2.putText(canvas, "Stickman Gor", (120, 370),
            cv2.FONT_HERSHEY_SIMPLEX, 0.8, white, 2, cv2.LINE_AA)

# Simpan hasil ke file
cv2.imwrite("stickman.png", canvas)

print("Gambar disimpan sebagai: stickman.png")

# Jika ingin menampilkan hasilnya secara lokal:
# cv2.imshow("Stickman", canvas)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
