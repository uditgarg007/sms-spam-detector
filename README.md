# 📧 SMS / Email Spam Detector

A **Machine Learning powered spam classification web application** that detects whether a given SMS message or email is **Spam** or **Ham (Not Spam)**.

The application uses **Natural Language Processing (NLP)** techniques along with a trained machine learning model to analyze text data and generate accurate predictions.

The model is deployed through an interactive web interface built using Streamlit.

---

## 🚀 Live Demo

🔗 **Try the App:**  
https://sms-spam-detector-udit.streamlit.app/

---

## 📌 Features

- Classifies **SMS messages or Emails** as Spam or Not Spam
- Instant **real-time prediction**
- Robust **text preprocessing pipeline**
- **TF-IDF vectorization** for feature extraction
- Interactive and lightweight **Streamlit web interface**
- Fast predictions using a **pre-trained machine learning model**

---

## 🧠 How the System Works

This project combines **Natural Language Processing (NLP)** with **Supervised Machine Learning** to detect spam messages.

### Workflow

1. **User Input**
   - The user enters a text message or email into the application.

2. **Text Preprocessing**
   - Convert text to lowercase
   - Remove punctuation and special characters
   - Tokenization (splitting text into words)
   - Remove English stopwords
   - Apply **Porter Stemming** to reduce words to their root form

3. **Feature Extraction**
   - The cleaned text is converted into numerical features using a **TF-IDF Vectorizer**.

4. **Prediction**
   - The vectorized text is passed to a **trained machine learning classifier** which predicts:
     - **Spam (1)**
     - **Not Spam / Ham (0)**

---

## 🛠️ Tech Stack

- **Python**
- **Streamlit**
- **Scikit-learn**
- **Pandas**
- **NLTK (Natural Language Toolkit)**
- **Pickle**

---

## 📂 Project Structure
sms-spam-detector
│
├── app.py # Streamlit web application
├── spam_classification.ipynb # Model training notebook
├── model.pkl # Trained spam classification model
├── vectorizer.pkl # TF-IDF vectorizer
├── requirements.txt # Python dependencies
└── README.md # Project documentation
