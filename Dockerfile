# Use a specific lightweight Python image
FROM python:3.11-alpine3.21

# Set the working directory inside the container
WORKDIR /src

# Copy only the requirements first to improve caching
COPY requirements.txt .

# Install dependencies
RUN RUN python -m pip install --upgrade pip && \
pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# Set a non-root user for security
RUN addgroup -S appgroup && adduser -S appuser -G appgroup
USER appuser

# Run the application
CMD ["python", "src/main.py"]
