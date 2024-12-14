# Use the official Python image
FROM python:3.9-slim

# Set the working directory
WORKDIR /client

COPY requirements.txt .

# Install pyepics library
RUN pip install --no-cache-dir -r requirements.txt
RUN apt-get update
RUN apt-get install procps -y

# Copy the Python script into the container
COPY engine.py .
COPY server.py .

# Run the Python script by default
CMD ["python", "server.py"]