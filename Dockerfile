### WARNING ###
# This file is not functional. It was just a test.

# Use official Python image as base
FROM python:3.11.8-slim

# Set working directory for the app
WORKDIR /app

# Install dependencies for Python server
COPY grid-simulator/requirements.txt /app
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port the server runs on
EXPOSE 5000

# Set working directory for SvelteKit app
WORKDIR /app/grid-sim-ui-client

# Install Node.js and npm
RUN apt-get update && apt-get upgrade -y && \
    apt-get install -y nodejs \
    npm     

# Install npm dependencies for SvelteKit app
COPY grid-sim-ui-client/package*.json ./
RUN npm install

# Copy SvelteKit app source code
COPY grid-sim-ui-client .

# Build the SvelteKit app
RUN npm run build

# Set the working directory back to the main app directory
WORKDIR /app

# Copy Python server code
COPY grid-simulator .

# Command to run the Python server
CMD ["python", "server.py"]
