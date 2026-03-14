import numpy as np
import cv2
import math


def chaotic_map(x, y, mu):
    x_new = (pow(x, math.pi**8) * math.e**4 + mu * y * math.e**10) % 1
    y_new = (pow(y, math.pi**8) * math.e**4 + mu * x_new * math.pi**9) % 1
    return x_new, y_new


def scramble_image(image_path, mu=0.5, x0=0.3, y0=0.7):

    img = cv2.imread(image_path)

    rows, cols, _ = img.shape

    x = x0
    y = y0

    xValues = []
    yValues = []

    for i in range(rows*cols):

        x, y = chaotic_map(x, y, mu)

        xValues.append(x)
        yValues.append(y)

    xValues = np.array(xValues)
    yValues = np.array(yValues)

    XPos = np.argsort(xValues[:rows])
    YPos = np.argsort(yValues[:cols])

    R_img = img[XPos, :, :]
    C_img = R_img[:, YPos, :]

    return C_img, XPos, YPos