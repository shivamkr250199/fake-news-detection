from flask import Flask, render_template, request
import joblib
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

nltk.download('stopwords')

# Load model and vectorizer
model = joblib.load('fake_news_model.pk1')
vectorizer = joblib.load('vectorizer.pk1')

# Text Preprocessing
port_stem = PorterStemmer()

def stemming(content):
    stemmed_content = []
    for text in content.split():
        cleaned_text = re.sub('[^a-zA-Z]', '', text)
        word = cleaned_text.lower()
        if word and word not in stopwords.words('english'):
            stemmed_content.append(port_stem.stem(word))
    return ' '.join(stemmed_content)

# Flask App
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    result = ''
    if request.method == 'POST':
        user_input = request.form['news']
        processed_input = stemming(user_input)
        vector_input = vectorizer.transform([processed_input])
        prediction = model.predict(vector_input)

        if prediction[0] == 1:
            result = '🟢 Real News'
        else:
            result = '🔴 Fake News'
    return render_template('index.html', result=result)

if __name__ == '__main__':
    import os
port = int(os.environ.get("PORT", 5000))  # fallback to 5000 for local testing
app.run(host='0.0.0.0', port=port)

