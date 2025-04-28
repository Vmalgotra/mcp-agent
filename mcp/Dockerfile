FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements first (cache pip install layer)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Now copy the rest of the app
COPY src/ .

# Create a non-root user
RUN adduser --disabled-password --gecos "" myuser

# Change ownership of app folder
RUN chown -R myuser:myuser /app

# Switch to the new user
USER myuser

# Set PATH properly
ENV PATH="/home/myuser/.local/bin:$PATH"

# Expose the application port
EXPOSE 8000

# Start the app
ENTRYPOINT ["python", "weather.py"]
