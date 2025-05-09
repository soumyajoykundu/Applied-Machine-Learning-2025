# SonicShield: AI-Powered Guardian Against DeepFake Speech

Welcome to **SonicShield**, a machine learning pipeline to detect AI-generated speech in real-time, aimed at combating DeepFake voice attacks. Developed by Team AudioSentinels as part of the Applied Machine Learning coursework.

## 🛡️ Project Overview

With the increasing misuse of generative AI for real-time voice cloning, SonicShield leverages classical ML models and transfer learning techniques to detect synthetic audio. Our goal is to build a reliable, low-latency detection system.

## 📂 Repository Structure
```
Project : SonicShield/
│
├── Code files/
│   ├── SonicShield_EDA_&_Data_Preprocessing.ipynb
│   ├── SonicShield_Modeling_Baseline.ipynb
│   └── SonicShield_TransferLearning.ipynb
│
├── Models/
│   ├── xgboost_best_model.pkl
│   └── distilbert_audio_classifier.pt
│
├── data-balanced.csv
│   └── [Processed feature files and audio segments]
│
├── SonicShield_Presentation.pdf
│   └── [slides of the study]
│
└── README.md
```

## 📊 Dataset

- Source: [Kaggle - DeepFake Voice Recognition](https://www.kaggle.com/datasets/birdy654/deep-voice-deepfake-voice-recognition/data)
- Consists of 8 real speakers and 56 fake conversions.
- Audio is processed into 1-second non-overlapping windows with extracted features like MFCCs, Spectral Centroid, Zero Crossing Rate, etc.

## 🛠️ Features Used

- Chromagram
- RMS Energy
- Spectral Centroid, Bandwidth, Rolloff
- Zero Crossing Rate
- 20 MFCCs

## 🤖 Models Trained

| Model                  | Accuracy | F1 Score | ROC AUC |
|------------------------|----------|----------|---------|
| XGBoost (Best)         | 0.993    | 0.993    | 0.993   |
| Random Forest          | 0.990    | 0.989    | 0.989   |
| Naive Bayes            | 0.830    | 0.822    | 0.830   |
| Logistic Regression    | 0.820    | 0.883    | 0.883   |
| SVM                    | 0.723    | 0.675    | 0.723   |

Also trained: DistilBERT-based Transfer Learning pipeline with 92.4% validation accuracy.

## 🧠 Transfer Learning

- Utilizes `distilbert-base-uncased` with 26-dimensional audio feature projection.
- Trained using HuggingFace's `Trainer` API.
- Logged via Weights & Biases.

## 📽️ Presentation

Check the [`SonicShield_Presentation.pdf`](SonicShield_Presentation.pdf) for an end-to-end overview of our workflow, challenges, and future scope.

## 👨‍💻 Team AudioSentinels

- Chandranath Bhattacharya — MDS202318  
- Salokya Deb — MDS202341  
- Soumyajoy Kundu — MDS202349  

_MSc. Data Science, Applied Machine Learning, May 2025_

