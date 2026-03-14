import numpy as np
import cv2
import math


def chaotic_map(x, y, mu):
    x_new = (pow(x, math.pi**8) * math.e**4 + mu * y * math.e**10) % 1
    y_new = (pow(y, math.pi**8) * math.e**4 + mu * x_new * math.pi**9) % 1
    return x_new, y_new


def generate_shares(logo_path, mu=0.5, x0=0.3, y0=0.7):

    logo = cv2.imread(logo_path, cv2.IMREAD_GRAYSCALE)

    _, logo_bin = cv2.threshold(logo, 127, 1, cv2.THRESH_BINARY)

    rows, cols = logo_bin.shape

    shares = []

    x = x0
    y = y0

    for share_index in range(3):

        chaotic_values = []

        for i in range(rows):
            for j in range(cols):

                x, y = chaotic_map(x, y, mu)

                chaotic_values.append(int((x + y) * 1000) % 2)

        share = np.array(chaotic_values).reshape(rows, cols)

        shares.append(share)

    share1, share2, share3 = shares

    share4 = share1 ^ share2 ^ share3 ^ logo_bin

    return share1, share2, share3, share4