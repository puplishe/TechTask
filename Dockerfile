# Use the official Python base image
FROM python:3.10-slim

# Set the working directory
WORKDIR /techtask

# Copy the app code to the container
ADD ./ /techtask/

COPY ./requirements.txt /techtask/

RUN apt-get update \
    && apt-get -y install libpq-dev python-dev-is-python3 gcc
# Install the dependencies

RUN pip install --upgrade pip

RUN pip install -r requirements.txt
# Expose the port
EXPOSE 8000

# Command to run the API server
CMD uvicorn app.main:app --host 0.0.0.0 --port 8000
