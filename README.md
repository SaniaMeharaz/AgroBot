🌱 AgroBot — Intelligent Plant Disease Diagnosis Assistant

A Smart Fusion of Computer Vision + NLP for Modern Agriculture

AgroBot is an advanced AI-driven plant disease diagnosis system designed to assist farmers, students, and researchers with instant disease prediction through leaf images and text-based symptom analysis.
This project integrates Deep Learning, Flask, and Natural Language Understanding to deliver fast, reliable, and user-friendly plant health insights.

✨ Why AgroBot?

✔ Modern agriculture demands quick decisions
✔ Farmers lose crops due to late diagnosis
✔ Manual inspection is slow and inaccurate

AgroBot solves this by providing:
🔍 1. Deep Learning Image Diagnosis

Upload any plant leaf → AgroBot identifies:

Disease Name

Cause

Symptoms

Treatment

Preventive Measures

💬 2. Smart Symptom-Based Chat Assistant

Type messages like:

my potato has brown spots


The AgroBot NLP engine understands your text and returns structured information:

Detected Symptom

Possible Diseases

Cause

Treatment

Prevention Tips

⚙️ 3. Clean & Simple Web Interface

Built with Flask + HTML/CSS, offering:

Image Upload Page

Chat Interface

Results Page

Smooth Navigation

🧠 Core Technologies Used
Layer	Technology
AI Model	TensorFlow, Keras, OpenCV
NLP Engine	Python rules-based matching
Backend	Flask
Frontend	HTML, CSS, JS
Deployment	GitHub, local Flask server
📁 Project Layout
AgroBot/
│── app.py               # Main Flask controller
│── plant_model.h5       # Trained CNN model
│── nlp_db.py            # Symptom → disease mapping
│── templates/           # UI pages
│── static/              # CSS & JS assets
│── test_images/         # For testing predictions
│── LICENSE              # MIT License
│── README.md            # Project documentation

🚀 How to Run Locally
1️⃣ Clone the repository
git clone https://github.com/SaniaMeharaz/AgroBot.git
cd AgroBot

2️⃣ Install dependencies
pip install -r requirements.txt

3️⃣ Start the server
python app.py

4️⃣ Access in browser
http://127.0.0.1:5000/

🎯 What Makes AgroBot Stand Out?

✨ AI + NLP combo
✨ Well-structured disease info
✨ Clean predictions
✨ Beginner-friendly codebase
✨ Expandable for future crops/datasets
✨ Accurate results from trained CNN model

🌱 Dataset

Model trained using the PlantVillage dataset, containing:

50,000+ labeled images

38 plant disease categories

