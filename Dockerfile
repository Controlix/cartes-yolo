# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Install system dependencies required by OpenCV and GLib
RUN apt-get update && apt-get install -y libgl1 libglib2.0-0

# Set the working directory in the container
WORKDIR /app

# Copy the dependencies file to the working directory
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the YOLO model file
COPY yolo11n.pt .

# Copy the content of the local src directory to the working directory
COPY train.py .

ENTRYPOINT ["python", "train.py"]
