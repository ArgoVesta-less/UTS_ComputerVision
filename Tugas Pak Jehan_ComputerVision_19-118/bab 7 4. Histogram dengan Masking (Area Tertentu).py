from matplotlib import pyplot as plt
import numpy as np
import cv2

def plot_histogram(image, title, mask=None):
    chans = cv2.split(image)
    colors = ("b", "g", "r")
    plt.figure()
    plt.title(title)
    plt.xlabel("Bins")
    plt.ylabel("# of Pixels")
    for (chan, color) in zip(chans, colors):
        hist = cv2.calcHist([chan], [0], mask, [256], [0, 256])
        plt.plot(hist, color=color)
    plt.xlim([0, 256])

image = cv2.imread("1302067.png")
cv2.imshow("Original", image)
plot_histogram(image, "Histogram for Original Image")

# Buat mask kotak
mask = np.zeros(image.shape[:2], dtype="uint8")
cv2.rectangle(mask, (15, 15), (130, 100), 255, -1)
cv2.imshow("Mask", mask)

# Terapkan mask
masked = cv2.bitwise_and(image, image, mask=mask)
cv2.imshow("Masked Image", masked)
plot_histogram(image, "Histogram for Masked Image", mask=mask)

plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
