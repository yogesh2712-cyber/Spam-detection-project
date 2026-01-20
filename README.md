# 📩 SMS Spam Detection using Machine Learning

## 📌 Project Overview
This project implements an end-to-end Machine Learning system to classify SMS messages as **Spam** or **Ham** using Natural Language Processing (NLP).

## 🎯 Objective
To build an automated spam detection model using real-world data and deploy it as a web application.

## 📂 Dataset
- Source: Kaggle (SMS Spam Collection Dataset)
- Total Records: 5,572
- Features:
  - Category (spam / ham)
  - Message (SMS text)

## 🔧 Tech Stack
- Python
- Pandas, NumPy
- Scikit-learn
- TF-IDF Vectorizer
- Naive Bayes Classifier
- Matplotlib (EDA)
- Streamlit & Flask (Deployment)

## ⚙️ Workflow
1. Data Collection
2. Data Cleaning & Preprocessing
3. Exploratory Data Analysis (EDA)
4. Feature Engineering using TF-IDF
5. Model Building using Naive Bayes
6. Pipeline Creation
7. Model Evaluation
8. Model Serialization using Pickle
9. Deployment using Streamlit

## 📊 Model Performance
- Accuracy: ~97%
- Efficient detection of spam messages

## 🚀 Deployment
The application is deployed using Streamlit and can be run locally using:
```bash
streamlit run app.py

# OUTPUT:
link : http://127.0.0.1:5000 