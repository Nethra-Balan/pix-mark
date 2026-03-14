import numpy as np
import cv2


def embed_share(scrambled_img, share):

    rows, cols, _ = scrambled_img.shape

    # resize share to match image size
    share_resized = cv2.resize(share.astype(np.uint8), (cols, rows), interpolation=cv2.INTER_NEAREST)

    R = scrambled_img[:,:,2]
    G = scrambled_img[:,:,1]
    B = scrambled_img[:,:,0]

    # extract MSB of R channel
    msb_R = (R >> 7) & 1

    # XOR operation
    embed_bits = share_resized ^ msb_R

    # replace LSB
    R_new = (R & 254) | embed_bits
    G_new = (G & 254) | embed_bits
    B_new = (B & 254) | embed_bits

    embedded = cv2.merge((B_new, G_new, R_new))

    return embedded