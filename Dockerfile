# Use Python as the base image
FROM python:3.13-slim

# Set working directory inside the container
WORKDIR /app

# Copy Python application into the container
COPY hospital_application.py .

# Run the application
CMD ["python", "-u", "hospital_application.py"]