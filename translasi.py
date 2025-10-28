import cv2
import numpy as np

# Buat kanvas hitam dan gambar stickman
canvas = np.zeros((400, 400, 3), dtype=np.uint8)
white = (255, 255, 255)

# Kepala
cv2.circle(canvas, (200, 100), 30, white, 2)
# Badan
cv2.line(canvas, (200, 130), (200, 250), white, 2)
# Tangan
cv2.line(canvas, (200, 160), (150, 200), white, 2)
cv2.line(canvas, (200, 160), (250, 200), white, 2)
# Kaki
cv2.line(canvas, (200, 250), (160, 320), white, 2)
cv2.line(canvas, (200, 250), (240, 320), white, 2)
# Nama
cv2.putText(canvas, "Stickman Gor", (120, 370),
            cv2.FONT_HERSHEY_SIMPLEX, 0.8, white, 2, cv2.LINE_AA)

# === Translasi (geser gambar) ===
tx, ty = 50, 40  # Geser kanan 50px dan ke bawah 40px
M = np.float32([[1, 0, tx], [0, 1, ty]])
translated = cv2.warpAffine(canvas, M, (400, 400))

# Simpan hasil
cv2.imwrite("stickman_translasi.png", translated)
print("Hasil translasi disimpan sebagai stickman_translasi.png")
