FROM alpine:3.17 as builder

# Install necessary packages
RUN apk add --no-cache python3 py3-pip libpq postgresql-client curl

# Add a non-root user
RUN adduser -D app

# Switch to the non-root user
USER app

# Set the working directory
WORKDIR /home/app

# Copy the application code
COPY . .

# Install Python dependencies
RUN pip3 install --user -r requirements.txt --no-cache-dir

# Set the PATH environment variable
ENV PATH="/home/app/.local/bin:$PATH"

# Expose the application port
EXPOSE 8000

# Start the application
CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]
