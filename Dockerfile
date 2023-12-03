# Use the official Python base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file to the working directory
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project directory to the working directory
COPY . .
RUN chmod +x entrypoint.sh
# Run the database initialization command: this will 
# bake an empty database in the container, so you can 
# not mount a volume over it, use this only for testing and if you need disposable db data
# RUN flask --app flaskapp init-db

# Set the environment variables
# Commented out as we are getting the values from
# the .env file
# ENV FLASK_APP=flaskapp
# ENV FLASK_RUN_HOST=0.0.0.0
# ENV FLASK_RUN_PORT=5000

# Expose the Flask application port
EXPOSE 5000

# Start the Flask application using Gunicorn
CMD ["./entrypoint.sh"]
