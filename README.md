🌱 AgroBot – Intelligent Multilingual Plant Disease Detection System (AI + CNN + NLP)

AgroBot is an AI-powered agricultural assistant that combines Deep Learning (CNN) for image-based plant disease classification and an NLP chatbot for symptom-based text queries.
Now upgraded with multilanguage support, allowing users to ask questions in any language (Telugu, Hindi, Tamil, English, etc.).

🚀 Overview

AgroBot is a complete intelligent system built with:

🧠 1. CNN Model (TensorFlow/Keras)

Detects plant leaf diseases from uploaded images.

💬 2. NLP-based Chatbot

Understands user messages like:

“My potato has brown spots”

“నా బెండకాయ ఆకు పసుపు రంగులోకి మారుతోంది”

“मेरे पत्तों पर काले धब्बे हैं”

🌐 3. Flask Web Application

User-friendly interface with:

Login page

Dashboard

Chat system

Image prediction box

🌏 4. Multilanguage Support

Auto-detects language → translates → processes → responds back in user's lang.

🖼️ Demo Workflow

1️⃣ Upload an image of a plant leaf
2️⃣ CNN model predicts the disease
3️⃣ NLP chatbot handles user text queries
4️⃣ Dashboard displays:

✔ Detected Disease
✔ Symptoms
✔ Causes
✔ Treatment
✔ Prevention
✔ Possible Alternative Diseases

🛠️ Tech Stack
Component-->Technology
Frontend-->HTML, CSS, Bootstrap
Backend-->Flask
AI Model-->CNN (TensorFlow, Keras)
NLP Engine-->Custom Symptom DB + Googletrans
Multilanguage-->langdetect, googletrans
Storage	Local uploads folder
Deployment	GitHub Pages, PythonAnywhere, Render
🧩 Key Features
1. Plant Disease Classification (CNN)

Real-time prediction from leaf images.

2. NLP Chatbot

Understands symptoms and replies with:

Disease

Cause

Treatment

Prevention

Possible diseases

3. Multilanguage Chat

Supports any language:

Hindi

Telugu

Tamil

Malayalam

English

Kannada

Bengali
…and more.

4. Login System

Simple username + password authentication.

Free and open-source.

📁 Project Structure
AgroBot/
│── app.py
│── nlp_db.py
│── plant_model.h5
│── requirements.txt
│── static/
│     └── uploads/
│── templates/
│     ├── index.html
│     ├── login.html
│     └── dashboard.html

⚙️ How to Run the Project
Step 1 — Install dependencies
pip install -r requirements.txt

Step 2 — Run the Flask app
python app.py

Step 3 — Open your browser
http://127.0.0.1:5000/

📦 requirements.txt 

If you want, I will create and upload the exact requirements file based on your final code.

📄 MIT License

This project is released under the MIT License — completely free to use, modify, and publish.

🌟 Why AgroBot?

Helps farmers detect diseases quickly

Reduces crop loss

Easy for students to understand

Simple yet powerful AI project

Perfect for final year projects, hackathons, and portfolios

🧭 Future Enhancements (Simple & Unique)

Mobile App version

Voice-enabled chatbot

Weather-based disease prediction

WhatsApp bot integration

Live camera disease detection
