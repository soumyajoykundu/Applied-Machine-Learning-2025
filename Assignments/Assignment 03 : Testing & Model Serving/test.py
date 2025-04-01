import pytest
from score import score
import pickle
import requests
import os
import time
import subprocess
import warnings
warnings.filterwarnings("ignore")

model = pickle.load(open("model_pipeline.pkl", "rb"))

# Test Cases
def test_smoke_test():
    '''
    Does the function produce some output without crashing? (smoke test)
    '''
    try:
        score("Example", model, 0.5)
    except Exception as e:
        pytest.fail(f"score function raised an exception: {e} (Smoke test failed)")
    
    assert type(score("Example", model, 0.5)) == tuple, f"Expected 2 outputs, received 1 (smoke test failed)"
    assert len(score("Example", model, 0.5)) == 2, f"Expected 2 outputs, received {len(score('Example', model, 0.5))} (smoke test failed)"

def test_format_test():
    '''
    Are the input/output formats/types as expected? (format test)
    '''
    text = "Example"
    threshold = 0.7
    prediction, probability = score(text, model, threshold)
    assert type(prediction) == int
    
    try:
        float(probability)
    except Exception as e:
        pytest.fail(f"score function raised an exception: {e} (Format test failed)")

def test_prediction_0_or_1():
    '''
    Is prediction value 0 or 1?
    '''
    text = "Example"
    threshold = 0.7
    prediction, _ = score(text, model, threshold)
    assert prediction in (0, 1)

def test_propensity_between_0_and_1():
    '''
    Is propensity score between 0 and 1?
    '''
    text = "Example"
    threshold = 0.7
    _, propensity = score(text, model, threshold)
    assert 0<=propensity<=1

def test_when_threshold_0_prediction_always_1():
    '''
    If you put the threshold to 0 does the prediction always become 1?
    '''
    text_1 = "Be there tonight"
    threshold = 0
    prediction, _ = score(text_1, model, threshold)
    assert prediction == 1
    
    text_2 = "Get a chance to go on a vacation to Hawaii"
    threshold = 0
    prediction, _ = score(text_2, model, threshold)
    assert prediction == 1

def test_when_threshold_1_prediction_always_0():
    '''
    If you put the threshold to 1 does the prediction always become 0?
    '''
    text_1 = "Be there tonight"
    threshold = 1
    prediction, _ = score(text_1, model, threshold)
    assert prediction == 0
    
    text_2 = "Get a chance to go on a vacation to Hawaii"
    threshold = 1
    prediction, _ = score(text_2, model, threshold)
    assert prediction == 0

def test_obvious_spam_gives_prediction_1():
    '''
    on an obvious spam input text is the prediction 1 
    '''
    text = '''Just apply to this lucky draw and get a chance to send
              your child to foreign universities like Stanford and Harvard. Don't be late. 
              Offer valid for a limited time only.'''
    threshold = 0.7
    prediction, _ = score(text, model, threshold)
    assert prediction == 1

def test_obvious_non_spam_gives_prediction_0():
    '''
    on an obvious non-spam input text is the prediction 0
    '''
    text = "Don't be late for tomorrow's meeting"
    threshold = 0.4
    prediction, _ = score(text, model, threshold)
    assert prediction == 0


def test_flask():
    # Start Flask with explicit host/port
    flask_process = subprocess.Popen(
        ["python", "app.py", "--host", "127.0.0.1", "--port", "5000"]
    )
    time.sleep(3)  # Increased wait time
    
    try:
        response = requests.post(
            "http://127.0.0.1:5000/score",
            json={"text": "TEST"},
            timeout=5
        )
        assert response.status_code == 200
    finally:
        flask_process.terminate()
        time.sleep(1)  # Cleanup time


## To run all the test cases, give input in the terminal as,
#  python -m pytest test.py -v

## ------------------ OUTPUT -----------------------

# ============================================= test session starts =============================================
# platform win32 -- Python 3.11.5, pytest-7.4.0, pluggy-1.0.0 -- C:\Users\skund\anaconda3\python.exe
# cachedir: .pytest_cache
# rootdir: D:\CMI DS\Sem IV\AML\Assignments\A3
# plugins: anyio-3.5.0, hydra-core-1.3.2
# collected 9 items                                                                                              

# test.py::test_smoke_test PASSED                                                                          [ 11%] 
# test.py::test_format_test PASSED                                                                         [ 22%] 
# test.py::test_prediction_0_or_1 PASSED                                                                   [ 33%] 
# test.py::test_propensity_between_0_and_1 PASSED                                                          [ 44%] 
# test.py::test_when_threshold_0_prediction_always_1 PASSED                                                [ 55%]
# test.py::test_when_threshold_1_prediction_always_0 PASSED                                                [ 66%] 
# test.py::test_obvious_spam_gives_prediction_1 PASSED                                                     [ 77%] 
# test.py::test_obvious_non_spam_gives_prediction_0 PASSED                                                 [ 88%]
# test.py::test_flask PASSED                                                                               [100%]

# ============================================== 9 passed in 7.00s ============================================== 