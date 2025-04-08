FROM python

# Set the working directory inside the container to /app
WORKDIR /app

# Copy the requirements.txt file into the container
COPY requirements.txt .

# Install Python dependencies listed in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy your application files into the container
COPY app.py .
COPY score.py .
COPY model_pipeline.pkl .

# Expose port 5000 to allow communication (e.g., for Flask apps)
EXPOSE 5000

# Define the command to run the app when the container starts
CMD ["python", "app.py"]
