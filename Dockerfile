FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy all files
COPY . .

# Install dependencies
RUN pip install -r app/requirements.txt

# Expose port
EXPOSE 5000

# Run Flask app
CMD ["python", "app/app.py"]
