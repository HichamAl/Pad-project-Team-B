# Base image
FROM python:3.9

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    python3-dev \
    libpq-dev \
    postgresql-client

# Set work directory
WORKDIR /pad

# Copy requirements
COPY requirements.txt requirements.txt

# Install requirements
RUN pip install -r requirements.txt

# Copy project
COPY . .

#Start Server
CMD python manage.py runserver

# django app port
EXPOSE 8000