# Use the official Python image from Docker Hub
FROM python:3.12-slim-bullseye


# Set the working directory inside the container
WORKDIR /app

# Install Poetry
RUN pip install --no-cache-dir poetry

# Copy the current directory contents into the container
COPY . /app

# Install virtual environment,
RUN python -m venv app/venv

# Copy pyproject.toml and poetry.lock (if available) to install dependencies first
COPY pyproject.toml poetry.lock* /app/

# Install project dependencies using Poetry
RUN poetry install

# Make port 80 available to the world outside this container (optional)
EXPOSE 5000

# Define environment variable (optional)
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Command to run your Python application
CMD ["python", "app.py"]
