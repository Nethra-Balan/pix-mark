import cv2
import numpy as np

def reconstruct_logo(share1, share2, share3, owner_path):

    owner = cv2.imread(owner_path, cv2.IMREAD_GRAYSCALE)

    # convert to binary
    _, owner = cv2.threshold(owner,127,1,cv2.THRESH_BINARY)

    # resize owner share if size mismatch
    if owner.shape != share1.shape:
        owner = cv2.resize(owner,
                           (share1.shape[1], share1.shape[0]),
                           interpolation=cv2.INTER_NEAREST)

    logo = share1 ^ share2 ^ share3 ^ owner

    return logo