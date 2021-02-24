# Base image
FROM python:alpine3.13

# Set a directory for the app
WORKDIR /usr/src/app

# Copy files required for the app to run, see .dockerignore
COPY . .

# Install python and pip
RUN pip3 install --upgrade pip && \
    pip3 install --no-cache-dir -r /usr/src/app/requirements.txt

# Tell the port number the container should expose
EXPOSE 5000

# Run the application
CMD ["python3", "/usr/src/app/app.py"]
