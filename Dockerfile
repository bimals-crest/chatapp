# Use official Python image as a base
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt if you have one, and install dependencies
# Assuming you will create a requirements.txt for all the dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . .

# Run migrations and collect static files for production
RUN python manage.py migrate
RUN python manage.py collectstatic --noinput

# Expose port 9090
EXPOSE 9090

# Start Django development server on the specified port
CMD ["python", "manage.py", "runserver", "0.0.0.0:9090"]
