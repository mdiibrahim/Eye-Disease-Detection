import base64
import io
import logging
import os

import gdown
import numpy as np
from PIL import Image
from flask import Flask, render_template, request
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

# Set up logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

app = Flask(__name__)

# Constants
MODEL_PATH = "models/eye_disease_model.h5"
DRIVE_URL = "https://drive.google.com/uc?id=11nt9ilopu9RmYIjCeAhOjaQbaREG3PG-"
CATEGORIES = ["Unknown", "Cataract", "Diabetic Retinopathy", "Glaucoma", "Normal"]

# Ensure model exists or download it
os.makedirs("models", exist_ok=True)
if not os.path.exists(MODEL_PATH):
    logging.warning("Model not found! Downloading from Google Drive...")
    gdown.download(DRIVE_URL, MODEL_PATH, quiet=False)

# Load Model
logging.info(f"Loading model from {MODEL_PATH}...")
model = load_model(MODEL_PATH)
logging.info("Model loaded successfully!")


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files["file"]
        if file:
            # Read and process image in memory
            img = Image.open(io.BytesIO(file.read())).convert("RGB")
            img_resized = img.resize((224, 224))
            img_array = image.img_to_array(img_resized)
            img_array = np.expand_dims(img_array, axis=0) / 255.0

            # Predict
            prediction = model.predict(img_array)
            result_index = np.argmax(prediction)
            result = CATEGORIES[result_index]
            confidence = float(np.max(prediction)) * 100
            logging.info(f"Prediction: {result} ({confidence:.2f}%)")

            # Convert image to base64 to show in result.html
            buffered = io.BytesIO()
            img.save(buffered, format="JPEG")
            img_base64 = base64.b64encode(buffered.getvalue()).decode("utf-8")
            img_data = f"data:image/jpeg;base64,{img_base64}"

            return render_template("result.html", result=result, confidence=confidence, img_path=img_data)

    return render_template("index.html")


if __name__ == "__main__":
    logging.info("Starting Flask app...")
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))
