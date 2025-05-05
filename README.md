# 🧠 Eye Disease Detection - Deep Learning Flask App

This is an AI-powered web application for detecting eye diseases from retinal images. It uses a custom-trained CNN based
on the VGG16 architecture.

---

### 🔗 Live Demo

**👉 [Click here to try the app](https://eye-disease-detection-wx8v.onrender.com/)**  
Hosted on [Render](https://render.com) — no installation needed.

---

## 🔍 Supported Eye Conditions

- 👁 Cataract
- 🩸 Diabetic Retinopathy
- 🌫 Glaucoma
- ✅ Normal
- ❓ Unknown (for cases the model can't classify confidently)

---

## 🚀 How It Works

1. Upload a retina image from your local system.
2. The image is preprocessed and fed into a CNN.
3. The model outputs the predicted class and confidence score.
4. The result is shown visually in the browser.

---

## 🧠 Model Info

- **Architecture**: Transfer learning using VGG16
- **Input Size**: 224 x 224
- **Framework**: TensorFlow + Keras
- **Classes**: ["Unknown", "Cataract", "Diabetic Retinopathy", "Glaucoma", "Normal"]

---

## 📁 File Structure

```
.
├── app.py                      # Flask web app
├── templates/
│   ├── index.html              # Upload page
│   └── result.html             # Result page
├── static/
│   └── styles.css              # Custom styles
├── models/
│   ├── eye_disease_model.h5    # Trained model (downloaded automatically)
│   └── eye_diseases_detection_vgg16.ipynb # Model training notebook
```

---

## 📦 Requirements

- Python 3.8+
- TensorFlow
- Flask
- Pillow
- NumPy
- gdown (for Google Drive file download)

Install all dependencies:

```bash
pip install -r requirements.txt
```

---

## 📥 Model Auto-Download

If `models/eye_disease_model.h5` is not found, the app automatically downloads it from:

👉 https://drive.google.com/file/d/11nt9ilopu9RmYIjCeAhOjaQbaREG3PG-/view

---

## 🖥 Run the App

```bash
python app.py
```

Visit `http://127.0.0.1:5000/` in your browser.

---

## 🤝 Contribution & Contact

This project is open for contributions! If you have suggestions, fixes, or ideas for improvement, feel free to open an
issue or PR.

- 📧 Email: mdiibrahim549@gmail.com
- 💼 LinkedIn: [Mohammad Ibrahim](https://www.linkedin.com/in/mdiibrahim/)

---

## ⚖️ License

This project is licensed under the [MIT License](LICENSE).
