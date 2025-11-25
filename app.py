from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import os
import tensorflow as tf
import numpy as np
import cv2
from nlp_db import SYMPTOM_DB, check_symptom
from googletrans import Translator
from langdetect import detect

app = Flask(__name__)
app.secret_key = "secret123"

translator = Translator()


# ------------------------------------------------------------
# LOAD MODEL
# ------------------------------------------------------------
try:
    model = tf.keras.models.load_model("plant_model.h5")
    print("✔ Model loaded successfully")
except Exception as e:
    print("Error loading model:", e)
    model = None


# ------------------------------------------------------------
# CLASS NAMES
# ------------------------------------------------------------
dataset_folder = "dataset"
class_names = sorted([
    f for f in os.listdir(dataset_folder)
    if os.path.isdir(os.path.join(dataset_folder, f))
]) if os.path.isdir(dataset_folder) else []


UPLOAD_FOLDER = "static/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


# ------------------------------------------------------------
# IMAGE PREDICTION FUNCTION
# ------------------------------------------------------------
def predict_image(img_path):
    try:
        img = cv2.imread(img_path)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = cv2.resize(img, (128, 128))
        img = img / 255.0
        img = np.expand_dims(img, axis=0)

        pred = model.predict(img)
        cls = np.argmax(pred)
        return class_names[cls]
    except:
        return "Prediction Failed"


# ------------------------------------------------------------
# CHATBOT API (MULTI-LANGUAGE)
# ------------------------------------------------------------
@app.route("/chatbot", methods=["POST"])
def chatbot():
    data = request.get_json(force=True)
    user_msg_original = (data.get("message") or "").strip()
    image_prediction = data.get("image_prediction")

    reply_parts = []

    # Detect language
    try:
        user_lang = detect(user_msg_original)
    except:
        user_lang = "en"

    # ------------------------------------------------------------
    # 1️⃣ TRANSLATE USER MESSAGE TO ENGLISH
    # ------------------------------------------------------------
    if user_msg_original:
        try:
            translated_to_en = translator.translate(user_msg_original, dest="en").text.lower()
        except:
            translated_to_en = user_msg_original.lower()
    else:
        translated_to_en = ""

    user_msg = translated_to_en

    # ------------------------------------------------------------
    # PROCESSING LOGIC (ALL NLP IN ENGLISH)
    # ------------------------------------------------------------

    # BOTH IMAGE + TEXT
    if image_prediction and user_msg:
        nlp_results = check_symptom(user_msg)
        reply_parts.append(f"🖼 Image Result: {image_prediction}\n")

        for result in nlp_results:
            for symptom, info in result.items():
                reply_parts.append(
                    f"🌿 Symptom from Text: {symptom}\n\n"
                    f"🦠 Possible Diseases: {', '.join(info.get('diseases', ['Not specified']))}\n\n"
                    f"🧬 Cause: {info.get('cause', 'Not specified')}\n\n"
                    f"💊 Treatment: {info.get('treatment', 'Not specified')}\n\n"
                    f"🛡 Prevention: {info.get('prevention', 'Not specified')}"
                )

    # ONLY TEXT
    elif user_msg:
        nlp_results = check_symptom(user_msg)
        for result in nlp_results:
            for symptom, info in result.items():
                reply_parts.append(
                    f"🌿 Symptom: {symptom}\n\n"
                    f"🦠 Possible Diseases: {', '.join(info.get('diseases', ['Not specified']))}\n\n"
                    f"🧬 Cause: {info.get('cause', 'Not specified')}\n\n"
                    f"💊 Treatment: {info.get('treatment', 'Not specified')}\n\n"
                    f"🛡 Prevention: {info.get('prevention', 'Not specified')}"
                )

    # ONLY IMAGE
    elif image_prediction:
        disease_data = SYMPTOM_DB.get(image_prediction)
        if disease_data:
            reply_parts.append(
                f"🖼 Disease Detected: {disease_data.get('name', image_prediction)}\n\n"
                f"🌿 Symptoms: {disease_data.get('symptoms', 'Not available')}\n\n"
                f"🧬 Cause: {disease_data.get('cause', 'Not available')}\n\n"
                f"💊 Treatment: {disease_data.get('treatment', 'Not available')}\n\n"
                f"🛡 Prevention: {disease_data.get('prevention', 'Not available')}"
            )
        else:
            reply_parts.append(
                f"🖼 Disease Detected: {image_prediction}\n"
                "No disease information available."
            )

    # NO INPUT
    else:
        reply_parts.append("I couldn't understand. Please type symptoms or upload a plant leaf image.")

    # ------------------------------------------------------------
    # 2️⃣ COMBINE REPLY IN ENGLISH
    # ------------------------------------------------------------
    final_reply_en = "\n\n".join(reply_parts)

    # ------------------------------------------------------------
    # 3️⃣ TRANSLATE BOT RESPONSE BACK TO USER LANGUAGE
    # ------------------------------------------------------------
    try:
        final_reply_translated = translator.translate(final_reply_en, dest=user_lang).text
    except:
        final_reply_translated = final_reply_en

    return jsonify({"reply": final_reply_translated})


# ------------------------------------------------------------
# DASHBOARD
# ------------------------------------------------------------
@app.route("/dashboard", methods=["GET", "POST"])
def dashboard():
    if "user" not in session:
        return redirect("/login")

    uploaded_image = None
    result = None

    if request.method == "POST" and "file" in request.files:
        file = request.files["file"]
        if file.filename:
            filepath = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(filepath)
            uploaded_image = file.filename

            pred = predict_image(filepath)

            if request.headers.get("X-Chat-Image") == "true":
                return jsonify({"prediction": pred})

    if request.method == "GET":
        session["chat"] = []

    return render_template(
        "dashboard.html",
        user=session["user"],
        chat=session.get("chat", []),
        uploaded_image=uploaded_image,
        result=result
    )


# ------------------------------------------------------------
# LOGIN, HOME, LOGOUT
# ------------------------------------------------------------
@app.route("/login", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if not username or not password:
            error = "Enter both username & password!"
        else:
            session["user"] = username
            session["chat"] = []
            return redirect("/dashboard")

    return render_template("login.html", error=error)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")


if __name__ == "__main__":
    app.run(debug=True)
