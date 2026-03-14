import cv2


def reconstruct_logo(share1, share2, share3, owner_share_path):

    owner = cv2.imread(owner_share_path, cv2.IMREAD_GRAYSCALE)

    owner = owner // 255

    logo = share1 ^ share2 ^ share3 ^ owner

    return logo