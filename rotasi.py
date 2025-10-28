import cv2
import numpy as np

# Buat kanvas dan gambar stickman
canvas = np.zeros((400, 400, 3), dtype=np.uint8)
white = (255, 255, 255)

cv2.circle(canvas, (200, 100), 30, white, 2)
cv2.line(canvas, (200, 130), (200, 250), white, 2)
cv2.line(canvas, (200, 160), (150, 200), white, 2)
cv2.line(canvas, (200, 160), (250, 200), white, 2)
cv2.line(canvas, (200, 250), (160, 320), white, 2)
cv2.line(canvas, (200, 250), (240, 320), white, 2)
cv2.putText(canvas, "Stickman Gor", (120, 370),
            cv2.FONT_HERSHEY_SIMPLEX, 0.8, white, 2, cv2.LINE_AA)

# === Rotasi (putar gambar) ===
center = (200, 200)
angle = 45  # derajat
scale = 1.0
M = cv2.getRotationMatrix2D(center, angle, scale)
rotated = cv2.warpAffine(canvas, M, (400, 400))

# Simpan hasil
cv2.imwrite("stickman_rotasi.png", rotated)
print("Hasil rotasi disimpan sebagai stickman_rotasi.png")
