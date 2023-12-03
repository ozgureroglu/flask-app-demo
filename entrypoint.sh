#!/bin/sh

# Path to the SQLite database file
DB_PATH="/app/instance/flaskapp.sqlite"

# Check if the database file exists
if [ ! -f "$DB_PATH" ]; then
    echo "Initializing the database..."
    echo "---------------------------\n"
    flask --app flaskapp init-db
    echo "\n"
else
    echo "Database already initialized!"
    echo "---------------------------\n"
fi

# Start the Flask application using Gunicorn
exec gunicorn --bind 0.0.0.0:5000 wsgi:app
