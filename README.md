# 📱 SMS Spam Classifier App

A lightweight Streamlit web app that classifies SMS messages as **Spam** or **Not Spam (Ham)** using a machine learning model trained on the classic SMS Spam Collection dataset.

---

## 🚀 Demo

**Try It Out**  
Paste an SMS message like:

> "Congratulations! You’ve won ₹50,000. Click to claim your prize now."

And get an instant prediction like: `🚨 Spam` or `✅ Not Spam`

---

## 🧠 Model Overview

This model uses:
- `TfidfVectorizer` for converting SMS text into numerical features.
- `SGDClassifier` (linear classifier with stochastic gradient descent) for spam classification.
- Trained and cross-validated in **Google Colab**, exported via `joblib`.

---

## 📂 Project Structure

```
spam-classifier-app/
├── app.py                   # 👉 Streamlit web app
├── spam_classifier.pkl      # ✅ Trained model (Tfidf + SGD pipeline)
├── requirements.txt         # 🔧 Python dependencies
├── README.md                # 📘 You're reading this
└── assets/
    └── banner.png           # 🖼️ (Optional) App banner/logo
```

---

## 🛠️ How to Run Locally

### 1. 🔃 Clone this repo

```bash
git clone https://github.com/yourusername/spam-classifier-app.git
cd spam-classifier-app
```

### 2. 🐍 Create virtual environment

```bash
python3 -m venv spam-env
source spam-env/bin/activate
```

### 3. 📦 Install dependencies

```bash
pip install -r requirements.txt
```

### 4. ▶️ Launch Streamlit app

```bash
streamlit run app.py
```

App will open in your browser at `http://localhost:8501`.

---

## 🧪 Example Messages to Test

| Message | Expected |
|--------|----------|
| "Hey, want to catch up at 7pm?" | ✅ Not Spam |
| "You have won ₹1,00,000! Click here to claim now!" | 🚨 Spam |
| "URGENT! Act now to claim your reward!" | 🚨 Spam |
| "Meet me at the office at 3pm" | ✅ Not Spam |

---

## 📊 Model Performance

| Metric    | Score |
|-----------|-------|
| Precision | 0.98+ |
| Recall    | 0.91+ |
| F1-Score  | 0.94+ |

Evaluated via 5-fold cross-validation on preprocessed SMS data.

---

## 📁 Dataset Used

- [SMS Spam Collection Dataset](https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset)
- 5.5k real SMS messages, labeled as `ham` or `spam`.

---

## ✅ Future Improvements

- Add support for email spam

- Use BERT/transformers for better feature extraction

- Build API endpoints for mobile integration

- Improve dataset diversity with modern scam patterns

## 🙌 Credits
- Developed by [Nilay Singh](https://github.com/n1lays1ngh)

- Trained using scikit-learn, hosted with Streamlit

- Dataset from UCI Machine Learning Repository

