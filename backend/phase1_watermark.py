from shares.generate_shares import generate_shares
from scrambling.scramble_image import scramble_image
from embedding.embed_share import embed_share
import cv2
import numpy as np


def inverse_permutation(img, XPos, YPos):

    inv_rows = np.argsort(XPos)
    inv_cols = np.argsort(YPos)

    row_restored = img[inv_rows,:,:]
    final_img = row_restored[:,inv_cols,:]

    return final_img


def phase1(original_img, logo_img):

    s1, s2, s3, owner_share = generate_shares(logo_img)

    # SAVE SHARES (add this)
    cv2.imwrite("output/share1.png", s1*255)
    cv2.imwrite("output/share2.png", s2*255)
    cv2.imwrite("output/share3.png", s3*255)

    scrambled, XPos, YPos = scramble_image(original_img)
    cv2.imwrite("output/scrambled_image.tiff", scrambled)
    np.save("output/XPos.npy", XPos)
    np.save("output/YPos.npy", YPos)

    embedded_scrambled = embed_share(scrambled, s1, s2, s3)

    watermarked = inverse_permutation(embedded_scrambled, XPos, YPos)

    cv2.imwrite("output/watermarked_image.tiff", watermarked)

    rows, cols, _ = watermarked.shape

    owner_resized = cv2.resize(
        owner_share.astype('uint8'),
        (cols, rows),
        interpolation=cv2.INTER_NEAREST
    )

    cv2.imwrite("output/owner_share.png", owner_resized*255)

    return watermarked