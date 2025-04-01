# **Assignment 3: Testing & Model Serving**

## **Overview**
This assignment focuses on testing a trained model for text classification and serving it using a Flask API. The objective is to implement unit tests for model scoring, integrate an endpoint for predictions, and generate a coverage report using `pytest`.

```
Assignment-3-Testing-Model-Serving/
├── app.py                     # Flask application for serving the model
├── score.py                   # Contains the score function for model prediction
├── test.py                    # Unit tests and integration tests for model scoring and Flask endpoint
├── coverage.txt               # Test and Score coverage report
├── model/
│   └── model_pipeline.pkl     # Saved model (CountVectorizer -> Logistic Regression) in `.pkl` format
└── README.md                  # Project overview and instructions
```
## **Unit Testing**
In `score.py`, implement a function to evaluate a trained model on a given text input. The unit tests in `test.py` validate various aspects of the scoring function, ensuring:
- **The function runs without errors** (smoke test).
- **The input/output formats** are correct.
- **Predictions are either 0 or 1**.
- **Propensity scores** range between 0 and 1.
- **Edge cases for threshold values** (0 and 1) behave as expected.
- **The model correctly identifies spam and non-spam text**.

## **Flask Serving**
A Flask application (`app.py`) is implemented with a `/score` endpoint that receives text as a POST request and returns predictions in **JSON** format.

## **Integration Testing**
Integration tests in `test.py` verify the Flask service by:
- **Launching the Flask app**.
- **Sending requests** to the `/score` endpoint.
- **Validating the response format and content**.
- **Closing the Flask app**.

## **Coverage Report**
The test coverage report (`coverage.txt`) is generated using `pytest` with coverage analysis to evaluate test completeness (`test.py` and `score.py`). The report includes details on uncovered lines and ensures robust testing practices.

---
For further details, refer to the official documentation:
- [**Pytest Documentation**](https://docs.pytest.org/en/8.0.x/)
- [**Flask Documentation**](https://flask.palletsprojects.com/en/2.3.x/quickstart/)
