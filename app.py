import streamlit as st
import pickle as pkl
import string
from nltk.corpus import stopwords
import nltk
from nltk.stem import porter
from nltk.tokenize import word_tokenize
from nltk.stem.porter import PorterStemmer

nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')
ps = PorterStemmer()


def transform_text(text):
  ps = PorterStemmer()
  text = text.lower()

  text = nltk.word_tokenize(text)

  y = []
  for i in text:
    if i.isalnum():
      y.append(i)

  text = y[:]
  y.clear()

  for i in text:
    if i not in stopwords.words("english") and i not in string.punctuation:
      y.append(i)

  text = y[:]
  y.clear()

  for i in text:
    y.append(ps.stem(i))

  return " ".join(y)

tfidf = pkl.load(open('vectorizer.pkl', 'rb'))
model = pkl.load(open('model.pkl', 'rb'))

st.title('Email/SMS Spam Detector')

input_txt = st.text_area('Enter The Message')

if st.button('Predict'):
  #preprocess
  trans = transform_text(input_txt)
  #vectorize
  vec_input = tfidf.transform([trans]).toarray()
  #predict
  result = model.predict(vec_input)
  #display
  if result[0] == 0:
      st.header("Not Spam")
  else:
      st.header("Spam")
