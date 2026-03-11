📧 SMS/Email Spam Detector
A Machine Learning-powered Spam Classifier built with Python and Streamlit that determines whether a given text message or email is Spam or Ham (Not Spam).



The system analyzes text data and computes predictions using Natural Language Processing (NLP) and machine learning techniques to generate highly accurate classifications.



🚀 Live Demo
🔗 https://sms-spam-detector-udit.streamlit.app/ (Update this link once deployed!)



📌 Features
Enter any text message or email into the text box

Get instant real-time classification (Spam or Not Spam)

Robust text preprocessing pipeline (tokenization, stemming, stop-word removal)

Interactive UI built using Streamlit

Fast and accurate predictions using a pre-trained ML model and TF-IDF vectorizer



🧠 How the Classification System Works
This project uses Natural Language Processing (NLP) and Supervised Machine Learning.

Steps
User inputs a raw text message or email.

The text undergoes preprocessing: converting to lowercase, tokenization, removing special characters/punctuation, and removing English stop words.

The remaining words are reduced to their root forms using Porter Stemming.

The cleaned text is converted into numerical vectors using a pre-trained TF-IDF Vectorizer.

The vectorized input is fed into a trained Machine Learning model to predict whether the message is Spam (1) or Not Spam (0).



🛠️ Tech Stack
Python

Pandas

Scikit-learn

NLTK (Natural Language Toolkit)

Streamlit

Pickle



📂 Project Structure
sms-spam-detector/
│
├── app.py
├── spam_classification.ipynb
├── vectorizer.pkl
├── model.pkl
├── requirements.txt
└── README.md
