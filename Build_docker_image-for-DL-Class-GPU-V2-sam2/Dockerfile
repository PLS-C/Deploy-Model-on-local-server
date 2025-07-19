# Use the NVIDIA CUDA base image with Ubuntu 22.04
FROM nvidia/cuda:11.8.0-cudnn8-runtime-ubuntu22.04

# Set environment variables for non-interactive installation
ENV DEBIAN_FRONTEND=noninteractive

# Update system and install Python, supervisor, and other necessary packages
RUN apt-get update && apt-get install -y \
    python3 python3-pip python3-dev \
    build-essential git wget curl supervisor && \
    apt-get clean && rm -rf /var/lib/apt/lists/*


# Upgrade pip
RUN python3 -m pip install --upgrade pip

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

#Install the ultralytics package from PyPI
RUN pip install ultralytics

#Install Deep sort Realtime
RUN pip install --no-cache-dir deep_sort_realtime

#Install flask gunicorn for serving optional (pip install flask-cors)
RUN pip install --no-cache-dir flask gunicorn
RUN pip install --no-cache-dir flask-cors

# Set the working directory
WORKDIR /workspace

#Clone SAM2
# Clone repository sam2
RUN git clone https://github.com/facebookresearch/sam2.git

# Install SAM2 as editable package
RUN pip install -e /workspace/sam2 && rm -rf /root/.cache

#Download the checkpoints
RUN cd /workspace/sam2/checkpoints && ./download_ckpts.sh

# Create the 'server' folder inside sam2
RUN mkdir -p /workspace/sam2/server

# Copy server script
COPY server.py /workspace/sam2/server/server.py

# Copy the supervisor configuration file
COPY supervisord.conf /etc/supervisor/supervisord.conf


# Expose Flask port and JupyterLab port
EXPOSE 8000 8888

# Command to start supervisor
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/supervisord.conf"]
