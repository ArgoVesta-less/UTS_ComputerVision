import numpy as np
import cv2

image = cv2.imread("1302067.png")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

eq = cv2.equalizeHist(gray)

cv2.imshow("Histogram Equalization", np.hstack([gray, eq]))
cv2.waitKey(0)
cv2.destroyAllWindows()
