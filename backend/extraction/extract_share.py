import numpy as np


def extract_shares(img):
    # image already loaded, do not use cv2.imread
    B = img[:,:,0]
    G = img[:,:,1]
    R = img[:,:,2]
    # Extract LSB
    lsb_R = R & 1
    lsb_G = G & 1
    lsb_B = B & 1
    # Extract MSB
    msb_R = (R >> 7) & 1
    msb_G = (G >> 7) & 1
    msb_B = (B >> 7) & 1
    # Recover shares
    share1 = lsb_R ^ msb_R
    share2 = lsb_G ^ msb_G
    share3 = lsb_B ^ msb_B
    return share1, share2, share3