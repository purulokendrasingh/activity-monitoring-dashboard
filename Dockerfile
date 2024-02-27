# Use the official Python image as a base image
FROM python:3.8.2-slim

# Set the working directory in the container
WORKDIR /app

# Copy the Flask app code into the container
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port that your Flask app runs on
EXPOSE 5000

# Command to run the Flask app
CMD ["python", "app.py"]
