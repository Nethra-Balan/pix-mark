import numpy as np
import cv2


def embed_share(scrambled_img, s1, s2, s3):
    rows, cols, _ = scrambled_img.shape
    # resize shares to match image size
    s1 = cv2.resize(s1.astype(np.uint8), (cols, rows), interpolation=cv2.INTER_NEAREST)
    s2 = cv2.resize(s2.astype(np.uint8), (cols, rows), interpolation=cv2.INTER_NEAREST)
    s3 = cv2.resize(s3.astype(np.uint8), (cols, rows), interpolation=cv2.INTER_NEAREST)
    B = scrambled_img[:,:,0]
    G = scrambled_img[:,:,1]
    R = scrambled_img[:,:,2]
    # extract MSB from each channel
    msb_R = (R >> 7) & 1
    msb_G = (G >> 7) & 1
    msb_B = (B >> 7) & 1
    # XOR operation
    R_bits = s1 ^ msb_R
    G_bits = s2 ^ msb_G
    B_bits = s3 ^ msb_B
    # replace LSB
    R_new = (R & 254) | R_bits
    G_new = (G & 254) | G_bits
    B_new = (B & 254) | B_bits
    embedded = cv2.merge((B_new, G_new, R_new))
    return embedded