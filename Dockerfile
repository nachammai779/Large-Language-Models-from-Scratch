# Use the official RunPod base image with Python 3.11
FROM runpod/base:0.6.2-cuda11.8.0

# Set working directory
WORKDIR /app

# Install Python dependencies
RUN pip install --no-cache-dir \
    runpod \
        tiktoken \
            matplotlib \
                numpy

                # Copy handler into the container
                COPY handler.py /app/handler.py

                # Start the RunPod serverless handler
                CMD ["python", "-u", "handler.py"]
