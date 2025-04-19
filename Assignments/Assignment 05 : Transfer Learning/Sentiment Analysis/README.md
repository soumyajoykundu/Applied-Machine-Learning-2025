## 💬 Sentiment Classifier using Transformer-based Transfer Learning

This project demonstrates how to use **transfer learning** with a pre-trained **Transformer model** (BERT) to classify text reviews into **positive**, **neutral**, and **negative** sentiments.

----------------------------------------

### 📁 Project Structure
```
Sentiment Analysis/
│
├── Sentiment_Analysis.ipynb   # Jupyter notebook
├── 5.2_data.zip               # Labeled sentiment dataset (from Kaggle)
└── README.md                  
```
----------------------------------------

### 📦 Dataset

- Source: https://www.kaggle.com/datasets/abhi8923shriv/sentiment-analysis-dataset
- Contains text samples labeled as:
  - 0: Negative
  - 1: Neutral
  - 2: Positive

----------------------------------------

### ⚙️ Model and Tools

- Pre-trained model: `bert-base-uncased` from Hugging Face Transformers
- Frameworks:
  - transformers
  - datasets
  - scikit-learn
  - pandas
- Fine-tuned using Hugging Face's Trainer API

----------------------------------------

### 🚀 How to Run?

1. Open the notebook in **Google Colab**.
2. Install dependencies:
   !pip install transformers datasets scikit-learn pandas

3. Upload the dataset `5.2_data.zip`.
4. Run all cells to train and evaluate the model.

----------------------------------------
----------------------------------------

## ✅ Notes

- You can swap the model (e.g., use RoBERTa or DistilBERT).
- Adjust max sequence length and tokenizer settings for optimization.

