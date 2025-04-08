# Assignment 4: Containerization & Continuous Integration

## Overview
* Docker-based containerization for the Flask model-serving app from Assignment 3.
* Automated testing using pytest.
* Git pre-commit hook for continuous integration.
* Coverage report for testing completeness.

Assignment-4-Containerization-CI/
├── app.py                 # Flask app serving the score function with basic HTML/CSS UI
├── score.py               # Function to predict spam using a pre-trained model
├── test.py                # Pytest suite for scoring logic, Flask API, and Docker container
├── model_pipeline.pkl     # Pre-trained model pipeline (CountVectorizer + Logistic Regression)
├── data_sms_spam.csv      # Dataset used for training/testing (included for completeness)
├── Dockerfile             # Instructions to build Docker container
├── requirements.txt       # Dependencies for app, testing, and Docker setup
├── test_results.txt       # Output from running pytest
├── coverage.txt           # Coverage report for test.py and score.py
├── pre-commit.txt         # Bash script for git pre-commit hook
└── README.md              # This file

## Docker Containerization

* The Dockerfile:
  * Installs required dependencies using requirements.txt
  * Copies app.py and score.py
  * Launches the app using: python app.py
  * Exposes port 5000

* To build and run the container:

    docker build -t spam-detector .
    docker run -p 5000:5000 spam-detector

## Testing & Coverage

* test.py includes:
  * Unit tests for score() function
  * Integration tests for /score Flask endpoint
  * Docker test that:
    * Builds and runs container using system commands
    * Sends test request to localhost:5000/score
    * Validates the response
    * Stops and removes the container

* To generate test results and coverage:

    pytest --tb=short --maxfail=1 > test_results.txt
    coverage run -m pytest
    coverage report > coverage.txt

## Pre-Commit Hook

* pre-commit.txt is a bash script for git pre-commit.
* Automatically runs test.py before every commit to main.
* If tests pass:
  * Commit proceeds
  * test_results.txt is staged
* If tests fail:
  * Commit is aborted

* To install the pre-commit hook:

    cp pre-commit.txt .git/hooks/pre-commit
    chmod +x .git/hooks/pre-commit

## References

* Docker Documentation: https://docs.docker.com/
* Pytest Documentation: https://docs.pytest.org/
* Git Hooks Documentation: https://git-scm.com/docs/githooks
