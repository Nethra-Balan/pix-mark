from phase1_watermark import phase1
from phase2_verify import phase2_verify


phase1("input/original.tiff","input/logo.tiff")

phase2_verify(
    "output/watermarked_image.tiff",
    "output/owner_share.png",
    "input/logo.tiff"
)