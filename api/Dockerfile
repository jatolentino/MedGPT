# medchatapi/Dockerfile

# Use the official Python image
# https://hub.docker.com/_/python
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Install dependencies
COPY medchatapi/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY medchatapi/ .

# Expose port 5000
EXPOSE 5000

# Run the Flask application
CMD ["python", "app.py"]
