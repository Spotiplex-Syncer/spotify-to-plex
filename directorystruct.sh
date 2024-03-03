#!/bin/bash
echo "What up"
# Define project structure
PROJECT_ROOT="splex"
DIRECTORIES=(
    "$PROJECT_ROOT/app/models"
    "$PROJECT_ROOT/app/routes"
    "$PROJECT_ROOT/app/services"
    "$PROJECT_ROOT/app/templates"
    "$PROJECT_ROOT/app/static/js"
    "$PROJECT_ROOT/app/static/css"
    "$PROJECT_ROOT/instance"
    "$PROJECT_ROOT/migrations"
)

echo "For dirs"
# Create directories
for dir in "${DIRECTORIES[@]}"; do
    mkdir -p "$dir"
done

# Create Python __init__.py files for packages
find "$PROJECT_ROOT/app" -type d -exec touch {}/__init__.py \;

# Create placeholder Python files
touch "$PROJECT_ROOT/app/models/models.py"
touch "$PROJECT_ROOT/app/routes/auth_routes.py"
touch "$PROJECT_ROOT/app/routes/sync_routes.py"
touch "$PROJECT_ROOT/app/services/spotify_service.py"
touch "$PROJECT_ROOT/app/services/plex_service.py"
touch "$PROJECT_ROOT/app/services/docker_service.py"
touch "$PROJECT_ROOT/celery_worker.py"
touch "$PROJECT_ROOT/run.py"

# Create placeholder templates
echo "<!DOCTYPE html><html><head><title>Login</title></head><body></body></html>" > "$PROJECT_ROOT/app/templates/login.html"
echo "<!DOCTYPE html><html><head><title>Dashboard</title></head><body></body></html>" > "$PROJECT_ROOT/app/templates/dashboard.html"
echo "<!DOCTYPE html><html><head><title>Progress</title></head><body></body></html>" > "$PROJECT_ROOT/app/templates/progress.html"
echo "<!DOCTYPE html><html><head><title>Layout</title></head><body>{{ content }}</body></html>" > "$PROJECT_ROOT/app/templates/layout.html"

# Create placeholder static files
echo "/* Style.css file */" > "$PROJECT_ROOT/app/static/css/style.css"
echo "// socketio.js file" > "$PROJECT_ROOT/app/static/js/socketio.js"

# Create a basic Dockerfile
cat <<EOF >"$PROJECT_ROOT/Dockerfile"
# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the current directory contents into the container at /usr/src/app
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV NAME World

# Run app.py when the container launches
CMD ["python", "run.py"]
EOF

# Create a basic docker-compose.yml
cat <<EOF >"$PROJECT_ROOT/docker-compose.yml"
version: '3'
services:
  web:
    build: .
    ports:
     - "5000:80"
    volumes:
     - .:/usr/src/app
EOF

# Create a basic requirements.txt
echo "Flask\nFlask-SocketIO\nFlask-Login\nDocker" > "$PROJECT_ROOT/requirements.txt"

# Feedback
echo "Project structure created successfully."
