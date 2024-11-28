# Use the official Python image from Docker Hub
FROM python:3.12-slim-bullseye

# Set the working directory in the container
WORKDIR /app

# Install Bash (to use 'source') and other necessary utilities
RUN apt-get update && apt-get install -y bash

# Install Poetry
RUN pip install --no-cache-dir poetry

# Set Poetry to create the virtual environment inside the project directory
RUN poetry config virtualenvs.in-project true

# Copy pyproject.toml and poetry.lock (if available) to install dependencies first
COPY pyproject.toml poetry.lock* /app/

# Install dependencies using Poetry and activate environment
RUN poetry install

RUN /bin/bash -c ". .venv/bin/activate"

# Copy the current directory contents into the container
COPY . .

# Expose the port FastAPI will run on
EXPOSE 8000

# Command to run the FastAPI application
CMD ["poetry", "run", "uvicorn", "main_cleo_api:app", "--host", "0.0.0.0", "--port", "8000"]
