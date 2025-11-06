from matplotlib import pyplot as plt
import cv2

# Baca gambar
image = cv2.imread("1302067.png")

# Ubah ke grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Original (Grayscale)", gray)

# Hitung histogram
hist = cv2.calcHist([gray], [0], None, [256], [0, 256])

# Tampilkan histogram
plt.figure()
plt.title("Grayscale Histogram")
plt.xlabel("Bins")
plt.ylabel("# of Pixels")
plt.plot(hist)
plt.xlim([0, 256])
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
