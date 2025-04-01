Assignment 3: Testing & Model Serving

Overview

This assignment focuses on testing a trained model for text classification and serving it using a Flask API. The objective is to implement unit tests for model scoring, integrate an endpoint for predictions, and generate a coverage report using pytest.

Unit Testing

In score.py, implement a function to evaluate a trained model on a given text input. The unit tests in test.py validate various aspects of the scoring function, ensuring:

The function runs without errors (smoke test).

The input/output formats are correct.

Predictions are either 0 or 1.

Propensity scores range between 0 and 1.

Edge cases for threshold values (0 and 1) behave as expected.

The model correctly identifies spam and non-spam text.

Flask Serving

A Flask application (app.py) is implemented with a /score endpoint that receives text as a POST request and returns predictions in JSON format.

Integration Testing

Integration tests in test.py verify the Flask service by:

Launching the Flask app.

Sending requests to the /score endpoint.

Validating the response format and content.

Closing the Flask app.

Coverage Report

The test coverage report (coverage.txt) is generated using pytest with coverage analysis to evaluate test completeness. The report includes details on uncovered lines and ensures robust testing practices.

For further details, refer to the official documentation:

Pytest Documentation

Flask Documentation

