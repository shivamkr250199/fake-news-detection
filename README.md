
# 📰 Fake News Detector 🔍

A simple yet powerful web app that detects whether a news headline or content is **Fake** or **Real** using **Machine Learning** and **Natural Language Processing (NLP)**.

🚀 Hosted on [Render](https://render.com)

render link[https://fake-news-detection-12.onrender.com]

---

## 🧠 How It Works

This app uses:
- ✅ **TF-IDF Vectorization** to convert text to numerical features
- ✅ **Logistic Regression** model trained on labeled news data
- ✅ **Flask** to serve a web interface
- ✅ **NLP techniques**: stopword removal, stemming, regex cleaning

---

## 🖥️ Demo

> Try it yourself!  
Enter a news statement and click **"Check News"** to know if it's **Real** or **Fake**.

![]

---

## 📁 Project Structure

```

fake-news-detector/
├── app.py                  # Main Flask app
├── requirements.txt        # Python dependencies
├── fake\_news\_model.pk1     # Trained ML model
├── vectorizer.pk1          # TF-IDF vectorizer
├── templates/
│   └── index.html          # Frontend HTML template
├── render.yaml             # Render deployment config
└── README.md               # This file!

````

---

## ⚙️ Installation

Clone the repo and install dependencies:

```bash
git clone https://github.com/shivamk250199/fake-news-detector.git
cd fake-news-detector
pip install -r requirements.txt
````

Run locally:

```bash
python app.py
```

Go to [http://localhost:5000](http://localhost:5000) in your browser.

---

## ☁️ Deploy on Render

This app is **Render-ready**. Just follow these steps:

1. Push to a public GitHub repo
2. Go to [Render](https://render.com)
3. Click **"New Web Service"**
4. Connect your repo and Render will auto-detect:

   * Python environment
   * `render.yaml` settings
5. Done! 🎉

---

## ✨ Features

* 🧠 Machine Learning-powered predictions
* 📊 Clean and simple interface
* 🔎 Preprocessing with stopword removal, stemming, and regex
* ☁️ Deploy-ready on Render

---

## 🛠️ Tech Stack

* Python
* Flask
* Scikit-learn
* NLTK
* HTML/CSS (Jinja Templates)
* Render (for deployment)

---

## 📌 Sample Usage

> **Input**:

```
Breaking: Scientists Discover Alien Life on Mars!
```

> **Output**:

```
🔴 Fake News
```

---

## 🧪 Future Improvements

* Add confidence scores for predictions
* Support full article analysis
* Improve accuracy with deep learning models
* Add a mobile-friendly UI

---

## 📄 License

This project is open-source and free to use under the [MIT License](LICENSE).

---

## 🤝 Contribute

Pull requests are welcome!
Feel free to fork this repo and improve the project.

---

## 💡 Author

Made with ❤️ by **Shivam Kumar**
📧 [Email me](mailto:shivamshandaliya1998@gmail.com
