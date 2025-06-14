# Use the NVIDIA CUDA base image with Ubuntu 22.04
FROM nvidia/cuda:11.8.0-cudnn8-runtime-ubuntu22.04

# Set environment variables for non-interactive installation
ENV DEBIAN_FRONTEND=noninteractive

# Update system and install Python, supervisor, and other necessary packages
RUN apt-get update && apt-get install -y \
    python3 python3-pip python3-venv python3-dev \
    build-essential git wget curl nano supervisor && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Check where supervisord is installed
RUN which supervisord

# Upgrade pip
RUN python3 -m pip install --upgrade pip

# Create a virtual environment named "dl_class-v1" and activate it
RUN python3 -m venv /opt/dl_class-v1
ENV PATH="/opt/dl_class-v1/bin:$PATH"

#Install Jupyter Lab
RUN pip install --no-cache-dir jupyterlab
#Install Scilkit-learn
RUN pip install --no-cache-dir scikit-learn
#Install Numpy
RUN pip install --no-cache-dir numpy
#Install pandas
RUN pip install --no-cache-dir pandas
#Install matplotlib
RUN pip install --no-cache-dir matplotlib
#Install Seaborn
RUN pip install --no-cache-dir seaborn
#Install image augmentation library
RUN pip install --no-cache-dir imgaug
#Install OpenCV
RUN pip install --no-cache-dir opencv-python-headless
#Install pytorch
RUN pip install --no-cache-dir torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
#Install torch summary
RUN pip install --no-cache-dir torch-summary
# Install the ultralytics package from PyPI
RUN pip install ultralytics
#Install Ult
RUN pip install --no-cache-dir torch-summary
#Install flask gunicorn for serving optional (pip install flask-cors)
RUN pip install --no-cache-dir flask gunicorn
RUN pip install --no-cache-dir flask-cors

# Set the working directory
WORKDIR /workspace

# Expose Flask port and JupyterLab port
EXPOSE 8000 8888

# Copy server script
COPY server.py /workspace/server.py

# Copy the supervisor configuration file
COPY supervisord.conf /etc/supervisor/supervisord.conf

# Command to start supervisor
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/supervisord.conf"]
