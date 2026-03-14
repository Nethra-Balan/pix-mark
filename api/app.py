from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os
import sys
import shutil

# allow backend imports
sys.path.append("../backend")

from phase1_watermark import phase1
from phase2_verify import phase2_verify

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = "../uploads"
RESULT_FOLDER = "../results"
BACKEND_OUTPUT = "output"   # folder expected by backend

# ensure folders exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(RESULT_FOLDER, exist_ok=True)
os.makedirs(BACKEND_OUTPUT, exist_ok=True)


@app.route("/phase1", methods=["POST"])
def watermark():

    original = request.files["original"]
    logo = request.files["logo"]

    original_path = os.path.join(UPLOAD_FOLDER, "original.tiff")
    logo_path = os.path.join(UPLOAD_FOLDER, "logo.tiff")

    original.save(original_path)
    logo.save(logo_path)

    # run backend phase1
    phase1(original_path, logo_path)

    # copy backend outputs to results folder
    shutil.copy("output/watermarked_image.tiff",
                "../results/watermarked_image.tiff")

    shutil.copy("output/owner_share.png",
                "../results/owner_share.png")

    shutil.copy("output/scrambled_image.tiff",
                "../results/scrambled_image.tiff")

    return jsonify({
        "watermarked": "/results/watermarked_image.tiff",
        "owner_share": "/results/owner_share.png"
    })


@app.route("/phase2", methods=["POST"])
def verify():

    suspect = request.files["suspect"]
    owner_share = request.files["owner_share"]
    logo = request.files["logo"]

    suspect_path = os.path.join(UPLOAD_FOLDER, "suspect.tiff")
    owner_path = os.path.join(UPLOAD_FOLDER, "owner.png")
    logo_path = os.path.join(UPLOAD_FOLDER, "logo.tiff")

    suspect.save(suspect_path)
    owner_share.save(owner_path)
    logo.save(logo_path)

    # run backend verification
    result, similarity = phase2_verify(
        suspect_path,
        owner_path,
        logo_path
    )

    # copy recovered logo
    shutil.copy("output/recovered_logo.png",
                "../results/recovered_logo.png")

    return jsonify({
        "result": result,
        "similarity": round(similarity, 2),
        "recovered_logo": "/results/recovered_logo.png"
    })


@app.route("/results/<filename>")
def download_file(filename):
    return send_from_directory(
        "../results",
        filename,
        as_attachment=True
    )


if __name__ == "__main__":
    app.run(debug=True, port=5000)