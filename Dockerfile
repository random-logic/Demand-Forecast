FROM python:3.12

# Set the working directory inside the container
WORKDIR /app

# Copy requirements.txt into the container
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Mount the current volume onto the container
VOLUME ["/app"]

# Default command to keep container running
CMD ["python3"]
