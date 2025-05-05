import os
import logging
import numpy as np
import base64
from flask import Flask, render_template, request
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from PIL import Image
import io

# Set up logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

app = Flask(__name__)

# Load Model
MODEL_PATH = "models/eye_disease_model.h5"
logging.info(f"Loading model from {MODEL_PATH}...")
model = load_model(MODEL_PATH)
logging.info("Model loaded successfully!")

# Updated class list (including Unknown)
CATEGORIES = ["Unknown", "Cataract", "Diabetic Retinopathy", "Glaucoma", "Normal"]

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files["file"]
        if file:
            # Load and preprocess image
            img = Image.open(io.BytesIO(file.read())).convert("RGB")
            img_resized = img.resize((224, 224))
            img_array = image.img_to_array(img_resized)
            img_array = np.expand_dims(img_array, axis=0) / 255.0

            # Predict
            prediction = model.predict(img_array)
            result_index = int(np.argmax(prediction))
            result = CATEGORIES[result_index]
            confidence = float(np.max(prediction)) * 100

            logging.info(f"Prediction: {result} ({confidence:.2f}%)")

            # Convert uploaded image to base64
            buffered = io.BytesIO()
            img.save(buffered, format="JPEG")
            img_base64 = base64.b64encode(buffered.getvalue()).decode("utf-8")
            img_data = f"data:image/jpeg;base64,{img_base64}"

            return render_template("result.html", result=result, confidence=confidence, img_path=img_data)

    return render_template("index.html")

if __name__ == "__main__":
    logging.info("Starting Flask app...")
    app.run(debug=True)
