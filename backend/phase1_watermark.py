from shares.generate_shares import generate_shares
from scrambling.scramble_image import scramble_image
from embedding.embed_share import embed_share
import cv2
import numpy as np


def inverse_permutation(img, XPos, YPos):

    rows, cols, _ = img.shape

    inv_rows = np.argsort(XPos)
    inv_cols = np.argsort(YPos)

    row_restored = img[inv_rows, :, :]
    final_img = row_restored[:, inv_cols, :]

    return final_img


def phase1(original_img, logo_img):

    s1, s2, s3, owner_share = generate_shares(logo_img)

    scrambled, XPos, YPos = scramble_image(original_img)

    np.save("output/XPos.npy", XPos)
    np.save("output/YPos.npy", YPos)

    embedded_scrambled = embed_share(scrambled, s1)

    # restore original ordering
    watermarked = inverse_permutation(embedded_scrambled, XPos, YPos)

    cv2.imwrite("output/watermarked_image.tiff", watermarked)
    cv2.imwrite("output/owner_share.png", owner_share * 255)

    return watermarked