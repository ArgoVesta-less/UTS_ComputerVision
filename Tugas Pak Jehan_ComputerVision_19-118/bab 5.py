import numpy as np
import cv2

# Membuat kanvas hitam ukuran 300x300
canvas = np.zeros((300, 300, 3), dtype="uint8")

# Warna hijau (B, G, R)
green = (0, 255, 0)
cv2.line(canvas, (0, 0), (300, 300), green)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

# Warna merah
red = (0, 0, 255)
cv2.line(canvas, (300, 0), (0, 300), red, 3)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

# Persegi panjang hijau (border default = 1px)
cv2.rectangle(canvas, (10, 10), (60, 60), green)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

# Persegi panjang merah dengan ketebalan garis 5px
cv2.rectangle(canvas, (50, 200), (200, 225), red, 5)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

# Persegi panjang biru terisi penuh
blue = (255, 0, 0)
cv2.rectangle(canvas, (200, 50), (225, 125), blue, -1)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

# Membuat ulang kanvas baru
canvas = np.zeros((300, 300, 3), dtype="uint8")
(centerX, centerY) = (canvas.shape[1] // 2, canvas.shape[0] // 2)
white = (255, 255, 255)

# Membuat lingkaran konsentris
for r in range(0, 175, 25):
    cv2.circle(canvas, (centerX, centerY), r, white)

cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

# Membuat 25 lingkaran acak
for i in range(0, 25):
    radius = np.random.randint(5, high=200)
    color = np.random.randint(0, high=256, size=(3,)).tolist()
    pt = np.random.randint(0, high=300, size=(2,))
    cv2.circle(canvas, tuple(pt), radius, color, -1)

cv2.imshow("Canvas", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()
