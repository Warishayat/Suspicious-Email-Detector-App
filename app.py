import streamlit as st
from sklearn.naive_bayes import GaussianNB
import pickle
import nltk
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import BernoulliNB
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

# Define the chat words dictionary
chat_words_dict = {
    "hello": "A greeting or expression of goodwill",
    # Add other chat words here...
}

stemmer = PorterStemmer()

def chatwordTreatment(text):
    if not isinstance(text, str):
        return " "
    corpus = []
    for i in text.split():
        if i in chat_words_dict:
            corpus.append(chat_words_dict[i])
        else:
            corpus.append(i)
    return " ".join(corpus)

def preprocessing(text):
    # Convert to lower case
    text = text.lower()
    # Tokenize text
    text = nltk.word_tokenize(text)
    # Remove special characters and extra spaces
    y = []
    for i in text:
        if i.isalnum() or i.isspace():
            y.append(i)
    text = y[:]
    y.clear()
    # Remove stopwords
    for i in text:
        if i not in stopwords.words("english"):
            y.append(i)
    text = y[:]
    y.clear()
    # Apply stemming
    for word in text:
        y.append(stemmer.stem(word))
    text = " ".join(y)
    y.clear()
    return text

# Load the model and vectorizer
with open('Model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('cv.pkl', 'rb') as f:
    vectorizer = pickle.load(f)

st.title("Suspecious Email Detector🕵️📧")
st.write("How may I assist you today?")

text = st.text_input("Enter your message here.")
text = chatwordTreatment(text)  # Chat word treatment
text = preprocessing(text)  # Preprocessing

# Ensure vectorizer is of correct type before transforming
if isinstance(vectorizer, CountVectorizer):
    vector = vectorizer.transform([text]).toarray()
else:
    st.write("Error: Vectorizer is not a CountVectorizer object")

button = st.button("SUBMIT")

if button:
    result = model.predict(vector)
    if result[0] == 0:
        st.success("Entered Mail is Not-Suspicious🕵️✅")
    else:
        st.success("Entered Mail has some Suspecious Content🕵️❌")
