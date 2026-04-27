# Dockerfile for Django App
# We use a slim Python image to keep the size down
FROM python:3.13.7-slim-trixie

# Set environment variables to prevent Python from writing bytecode files
# and to ensure stdout and stderr are unbuffered.
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

# Set the working directory in the container
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Copy the application code into the container
COPY . .

# Expose the port the Django app will run on
EXPOSE 8000

# Command to run the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]