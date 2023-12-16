from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np
import nltk
import re
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer

nltk.download('stopwords')
nltk.download('punkt')

# Function to clean punctuations
def cleaning_punctuations(text):
    english_punctuations = string.punctuation
    translator = str.maketrans('', '', english_punctuations)
    return text.translate(translator)

# Function to clean repeating characters
def cleaning_repeating_char(text):
    return re.sub(r'(.)\1+', r'\1', text)

# Function to clean URLs
def cleaning_URLs(text):
    return re.sub(r'((www\.[^\s]+)|(https?://[^\s]+))', ' ', text)

# Function to clean numbers
def cleaning_numbers(text):
    return re.sub(r'[0-9]+', '', text)

# Get English stopwords
english_stopwords = set(stopwords.words('english'))

# Function to remove stopwords
def remove_stopwords(text):
    tokens = word_tokenize(text)
    filtered_tokens = [word for word in tokens if word.lower() not in english_stopwords]
    return ' '.join(filtered_tokens)

# Initialize NLTK stemmer and lemmatizer
st = PorterStemmer()
lm = WordNetLemmatizer()

# Create Flask app
app = Flask(__name__)

# Load the pickle model
with open('LRmodel.pkl', 'rb') as file:
    lr_model = pickle.load(file)


# Load the vectorizer
with open('vectorizer.pkl', 'rb') as file:
    vectoriser = pickle.load(file)

@app.route("/")
def Home():
    return render_template("index.html")

# Define a route for the prediction endpoint
@app.route('/predict', methods=["POST"])

def predict():
    text = request.form['Review']  # Get the review from the form

    #Preprocess the review
    text = text.lower()
    text = cleaning_punctuations(text)
    text = cleaning_repeating_char(text)
    text = cleaning_URLs(text)
    text = cleaning_numbers(text)
    text = remove_stopwords(text)

    # Tokenize, stem, and lemmatize
    tokens = word_tokenize(text)
    stemmed_tokens = [st.stem(token) for token in tokens]
    lemmatized_tokens = [lm.lemmatize(token) for token in stemmed_tokens]

    text= ' '.join(lemmatized_tokens)
    print(text)

    
   

    text_vector = vectoriser.transform([text])

    # Predict sentiment
    prediction = lr_model.predict(text_vector)

    # Convert the prediction to sentiment labels
    sentiment = "positive" if prediction[0] == 1 else "negative"

    return render_template("index.html", prediction_text="The sentiment is {}".format(sentiment))

# Run the app if executed directly
if __name__ == "__main__":
    app.run(debug=True)