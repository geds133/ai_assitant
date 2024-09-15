# Use the official Python image from Docker Hub
FROM python:3.12-slim-bullseye


# Set the working directory inside the container
WORKDIR /app

# Install Bash (to use 'source') and other necessary utilities
RUN apt-get update && apt-get install -y bash

# Install Poetry
RUN pip install --no-cache-dir poetry

# Set Poetry to create the virtual environment inside the project directory
RUN poetry config virtualenvs.in-project true

# Install virtual environment,
RUN python -m venv app/venv

# Copy pyproject.toml and poetry.lock (if available) to install dependencies first
COPY pyproject.toml poetry.lock* /app/

# Install dependencies using Poetry and activate environment
RUN /bin/bash -c "poetry install --no-root"

RUN /bin/bash -c ". .venv/bin/activate"

# Copy the current directory contents into the container
COPY . .

# Make port 80 available to the world outside this container (optional)
EXPOSE 5000

# Define environment variable (optional)
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PATH="/app/.venv/bin:$PATH"

# Command to run your Python application
CMD ["poetry", "run", "python", "src/app/app.py"]
