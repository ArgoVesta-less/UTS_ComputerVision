from __future__ import print_function
from matplotlib import pyplot as plt
import numpy as np
import cv2

image = cv2.imread("1302067.png")
cv2.imshow("Original", image)

# Pisahkan channel warna
chans = cv2.split(image)
colors = ("b", "g", "r")

# Plot histogram 1D
plt.figure()
plt.title("Flattened Color Histogram")
plt.xlabel("Bins")
plt.ylabel("# of Pixels")
for (chan, color) in zip(chans, colors):
    hist = cv2.calcHist([chan], [0], None, [256], [0, 256])
    plt.plot(hist, color=color)
plt.xlim([0, 256])

# Histogram 2D (kombinasi channel)
fig = plt.figure()

ax = fig.add_subplot(131)
hist = cv2.calcHist([chans[1], chans[0]], [0, 1], None, [32, 32], [0, 256, 0, 256])
p = ax.imshow(hist, interpolation="nearest")
ax.set_title("2D Histogram G dan B")
plt.colorbar(p)

ax = fig.add_subplot(132)
hist = cv2.calcHist([chans[1], chans[2]], [0, 1], None, [32, 32], [0, 256, 0, 256])
p = ax.imshow(hist, interpolation="nearest")
ax.set_title("2D Histogram G dan R")
plt.colorbar(p)

ax = fig.add_subplot(133)
hist = cv2.calcHist([chans[0], chans[2]], [0, 1], None, [32, 32], [0, 256, 0, 256])
p = ax.imshow(hist, interpolation="nearest")
ax.set_title("2D Histogram B dan R")
plt.colorbar(p)

print("2D histogram shape:", hist.shape)

# Histogram 3D
hist = cv2.calcHist([image], [0, 1, 2], None, [8, 8, 8], [0, 256, 0, 256, 0, 256])
print("3D histogram shape:", hist.shape, "dengan", hist.flatten().shape[0], "nilai")

plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
