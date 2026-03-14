from extraction.extract_share import extract_shares
from reconstruction.reconstruct_logo import reconstruct_logo
import numpy as np
import cv2


def apply_scramble(img, XPos, YPos):
    """
    Apply the same scrambling used in Phase-1
    """

    row_scrambled = img[XPos, :, :]
    col_scrambled = row_scrambled[:, YPos, :]

    return col_scrambled


def verify_logo(original_logo_path, recovered_logo):

    original = cv2.imread(original_logo_path, cv2.IMREAD_GRAYSCALE)

    _, original = cv2.threshold(original,127,1,cv2.THRESH_BINARY)

    recovered_resized = cv2.resize(
        recovered_logo,
        (original.shape[1], original.shape[0]),
        interpolation=cv2.INTER_NEAREST
    )

    similarity = np.sum(original == recovered_resized) / original.size

    return similarity


def phase2_verify(suspect_image, owner_share, original_logo):

    img = cv2.imread(suspect_image)

    # load scrambling keys from Phase-1
    XPos = np.load("output/XPos.npy")
    YPos = np.load("output/YPos.npy")

    # scramble again before extraction
    scrambled = apply_scramble(img, XPos, YPos)

    # extract embedded shares
    s1, s2, s3 = extract_shares(scrambled)

    # reconstruct watermark
    logo = reconstruct_logo(s1, s2, s3, owner_share)

    cv2.imwrite("output/recovered_logo.png", logo*255)

    similarity = verify_logo(original_logo, logo)

    if similarity > 0.8:
        result = "Copyright Verified"
    else:
        result = "Copyright Not Verified"

    print("Verification Result:", result)
    print("Similarity:", similarity*100,"%")

    return result