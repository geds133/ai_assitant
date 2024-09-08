# Use the official Python image from Docker Hub
FROM python:3.12.5-alpine3.20

# Set the working directory inside the container
WORKDIR /app

# Install Poetry
RUN pip install --no-cache-dir poetry

# Copy the current directory contents into the container
COPY . /app

# Install virtual environment,
RUN python -m venv app-env

# Activate the virtual environment and install dependencies
RUN /bin/bash -c "source /app/my_custom_env/bin/activate && poetry install

# Make port 80 available to the world outside this container (optional)
EXPOSE 80

# Define environment variable (optional)
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Command to run your Python application
CMD ["bash"]
