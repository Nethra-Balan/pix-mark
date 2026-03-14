from scrambling.scramble_image import scramble_image
import cv2

scrambled, XPos, YPos = scramble_image("input/original.tiff")

cv2.imwrite("output/scrambled.tiff", scrambled)