# 🧠 Eye Disease Detection - Deep Learning Flask App

This is an AI-powered web application for detecting eye diseases from retinal images using a deep learning model built
with transfer learning. It offers a simple web interface powered by Flask where users can upload an image and receive a
prediction instantly.

---

## 🔍 Supported Eye Conditions

The model can classify retinal fundus images into the following categories:

- 👁 Cataract
- 🩸 Diabetic Retinopathy
- 🌫 Glaucoma
- ✅ Normal (Healthy Retina)
- ❓ Unknown (If the image doesn't match known patterns)

---

## 🚀 How It Works

1. Upload a retina image from your local device.
2. The image is preprocessed (resized to 224x224 and normalized).
3. It is passed through a custom-trained CNN based on the VGG16 architecture.
4. The model returns the most probable class and a confidence score.
5. Low-confidence or "Unknown" results are displayed with a warning.

---

## 🧠 Model Info

- **Architecture**: VGG16 (Transfer Learning)
- **Framework**: TensorFlow + Keras
- **Input Size**: 224 x 224
- **Classes**:
  ["Unknown", "Cataract", "Diabetic Retinopathy", "Glaucoma", "Normal"]

The model is trained on high-resolution retinal datasets and is capable of handling real-world inputs with fairly good
accuracy.

---

## 📁 File Structure

.
├── app.py # Flask web app
├── templates/
│ ├── index.html # Upload page
│ └── result.html # Result page
├── static/
│ └── styles.css # Custom styles
├── models/
│ ├── eye_disease_model.h5 # Trained model (downloaded automatically)
│ └── eye_diseases_detection_vgg16.ipynb # Model training notebook

---

## 📥 Auto Model Download

If the model file `models/eye_disease_model.h5` is not found, the app will automatically download it from the link
below:

🔗 https://drive.google.com/file/d/11nt9ilopu9RmYIjCeAhOjaQbaREG3PG-/view

No manual download required.

---

## 🖥 How to Run

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Run the Flask App
python app.py

# 3. Open in browser
http://127.0.0.1:5000/
```

---

## ✅ Features

- Fast predictions with real-time feedback
- Confidence scores shown with safety warnings
- Automatically handles unknown or unclassified images
- User-friendly UI built with HTML + CSS
- Image preview and error validation
- Works locally and offline after setup

---

## 📢 Contribution Guide

This project is **open for contributions**!

If you'd like to improve:

- The model accuracy
- Add new diseases
- Enhance the frontend
- Optimize performance

Please feel free to **fork** the repo, make your changes, and open a **pull request**.

---

## 📜 License

This project is licensed under the **MIT License** — meaning you're free to use, modify, and distribute it with
attribution.

---

## 👨‍💻 Connect with Me

I’m always open to collaboration or feedback:

- 📧 Email: mdiibrahim549@gmail.com
- 💼 LinkedIn: https://www.linkedin.com/in/mdiibrahim/

Let's build better healthcare tools together 💡