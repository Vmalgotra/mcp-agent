FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy agent - Start
COPY weather_agent/ /app/multi_tool_agent/
# Copy agent - End

# Create a non-root user
RUN adduser --disabled-password --gecos "" myuser

# Change ownership of /app to myuser
RUN chown -R myuser:myuser /app

# Switch to the non-root user
USER myuser

# Set up environment variables - Start
ENV PATH="/home/myuser/.local/bin:$PATH"
#ENV GOOGLE_GENAI_USE_VERTEXAI=1
#ENV GOOGLE_CLOUD_PROJECT=d11-torque
#ENV GOOGLE_CLOUD_LOCATION=us-central1

RUN pwd

RUN ls

EXPOSE 8000

CMD adk web --port=8000  "/app"
