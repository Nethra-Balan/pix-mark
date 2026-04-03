import cv2
import numpy as np
from skimage.metrics import structural_similarity as ssim


def calculate_psnr(img1, img2):
    mse = np.mean((img1.astype(np.float32) - img2.astype(np.float32)) ** 2)
    if mse == 0:
        return float('inf')
    return 20 * np.log10(255.0 / np.sqrt(mse))


def calculate_ssim(img1, img2):
    gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

    score, _ = ssim(gray1, gray2, full=True)
    return score


def evaluate(img_path1, img_path2, title=""):

    img1 = cv2.imread(img_path1)
    img2 = cv2.imread(img_path2)

    if img1 is None or img2 is None:
        print("Error loading images")
        return

    # Resize if sizes differ
    img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))

    psnr_val = calculate_psnr(img1, img2)
    ssim_val = calculate_ssim(img1, img2)

    print(f"\n--- {title} ---")
    print("PSNR:", psnr_val)
    print("SSIM:", ssim_val)

    return psnr_val, ssim_val


if __name__ == "__main__":

    # 1️⃣ Image Quality (MANDATORY)
    evaluate(
        "input/original.tiff",
        "output/watermarked_image.tiff",
        "Original vs Watermarked"
    )

    