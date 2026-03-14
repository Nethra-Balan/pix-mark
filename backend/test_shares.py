from shares.generate_shares import generate_shares
import cv2

s1, s2, s3, s4 = generate_shares("input/logo.tiff")

cv2.imwrite("output/share1.png", s1*255)
cv2.imwrite("output/share2.png", s2*255)
cv2.imwrite("output/share3.png", s3*255)
cv2.imwrite("output/owner_share.png", s4*255)