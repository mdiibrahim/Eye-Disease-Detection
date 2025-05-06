import base64  # To convert image data to base64 so it can be displayed in HTML
import io  # To handle in-memory file objects (like images from uploads)
import logging  # For logging important info and debugging messages
import os  # To handle file and folder paths

import gdown  # To download files from Google Drive
import numpy as np  # For numerical operations and arrays
from PIL import Image  # To open, resize, and convert uploaded images
from flask import Flask, render_template, request  # Flask tools to build the web app
from tensorflow.keras.models import load_model  # To load the saved deep learning model
from tensorflow.keras.preprocessing import image  # To convert images into model-readable arrays

# ---------------------------------------------
# Setup logging: This helps track what's going on in the app
# INFO level shows all useful progress and debug messages in console
# ---------------------------------------------
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# ---------------------------------------------
# Create the Flask app instance
# This is the core web app
# ---------------------------------------------
app = Flask(__name__)

# ---------------------------------------------
# Configuration variables
# You can change these if your model or labels are different
# ---------------------------------------------
MODEL_PATH = "models/eye_disease_model.h5"  # Location of the trained model file
DRIVE_URL = "https://drive.google.com/uc?id=11nt9ilopu9RmYIjCeAhOjaQbaREG3PG-"  # Backup URL to download the model
CATEGORIES = ["Unknown", "Cataract", "Diabetic Retinopathy", "Glaucoma",
              "Normal"]  # Class labels predicted by the model

# ---------------------------------------------
# Check if model file exists locally
# If not, download it from Google Drive
# ---------------------------------------------
os.makedirs("models", exist_ok=True)  # Make sure the 'models' folder exists

if not os.path.exists(MODEL_PATH):
    logging.warning("Model not found! Downloading from Google Drive...")
    gdown.download(DRIVE_URL, MODEL_PATH, quiet=False)  # Download the model file

# ---------------------------------------------
# Load the model into memory
# This allows it to be used for predictions
# ---------------------------------------------
logging.info(f"Loading model from {MODEL_PATH}...")
model = load_model(MODEL_PATH)
logging.info("Model loaded successfully!")


# ---------------------------------------------
# Home route: Handles both GET and POST requests
# GET shows the upload page
# POST handles image upload and prediction
# ---------------------------------------------
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files["file"]  # Get the uploaded image file from the form

        if file:
            # 🔄 Read the uploaded image and convert it to RGB (in case it's grayscale or CMYK)
            img = Image.open(io.BytesIO(file.read())).convert("RGB")

            # 📏 Resize the image to 224x224 pixels — this is what VGG16 expects
            img_resized = img.resize((224, 224))

            # 🔢 Convert the image to a NumPy array
            img_array = image.img_to_array(img_resized)

            # 🧼 Normalize the pixel values (0–255 ➡ 0–1) and add batch dimension
            img_array = np.expand_dims(img_array, axis=0) / 255.0

            # 🤖 Make prediction with the model
            prediction = model.predict(img_array)

            # 🎯 Get the index of the class with the highest predicted probability
            result_index = np.argmax(prediction)

            # 🏷️ Get the label name using the index
            result = CATEGORIES[result_index]

            # 📊 Get the confidence score (probability) and convert it to a percentage
            confidence = float(np.max(prediction)) * 100
            logging.info(f"Prediction: {result} ({confidence:.2f}%)")

            # 🖼️ Convert the image to base64 so we can display it directly in HTML
            buffered = io.BytesIO()
            img.save(buffered, format="JPEG")
            img_base64 = base64.b64encode(buffered.getvalue()).decode("utf-8")
            img_data = f"data:image/jpeg;base64,{img_base64}"

            # ⏎ Render the result page with the prediction info
            return render_template(
                "result.html",
                result=result,
                confidence=confidence,
                img_path=img_data
            )

    # 🖐️ If it's a GET request (no file submitted), just show the upload form
    return render_template("index.html")


# ---------------------------------------------
# This runs the Flask app locally on port 5000
# 0.0.0.0 makes it accessible on any network IP
# ---------------------------------------------
if __name__ == "__main__":
    logging.info("Starting Flask app...")
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))
