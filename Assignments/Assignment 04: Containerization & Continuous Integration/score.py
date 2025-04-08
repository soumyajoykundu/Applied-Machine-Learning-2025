import pickle
from sklearn.pipeline import Pipeline

def score(text: str, model: Pipeline, threshold: float) -> tuple[bool, float]:
    """
    Score text for spam or ham.
    """
    propensity = model.predict_proba([text])[0][1]  # P(spam)
    if propensity >= threshold:
        prediction = 1 # spam
    else:
        prediction = 0 # ham
    return prediction, propensity

# Example (for testing)
if __name__ == "__main__":
    model = pickle.load(open("model_pipeline.pkl", "rb"))
    print(score("Congratulations! You've won a $1000 gift card. Click here to claim your prize now.", model, 0.5))  
    print(score("Hello, how are you?", model, 0.5)) 


## -------------- OUTPUT (for examples) -------------------

# (1, 0.9842301695479573)
# (0, 0.002228629170326061)
