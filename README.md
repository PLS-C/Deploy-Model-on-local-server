# Deploy-Model-on-local-server
this example is show how to create a docker image for deploy the model with GPU on local server in windows os

## ✅ Prerequisites
- Docker desktop
- Windows Subsystem for Linux (WSL) (Ubuntu)
- NVIDIA GPU

### 1 Check the WSL

To check the Ubuntu version inside WSL via PowerShell, you can use this command:

```batch
wsl cat /etc/os-release
```

To list all installed WSL distros:

```batch
wsl --list --verbose
```

### 2 Check the docker

- Check docker version

```batch
 docker --version
```

## Install Ubuntu in WSL
### 1. List available WSL distros:
Run in PowerShell:
```power shell
wsl --list --online
```
### 2. Install Ubuntu (e.g., Ubuntu 22.04):
```power shell
wsl --install -d Ubuntu-22.04
```

### 3. Verify installation
- After it installs, check again:
```batch
wsl -l -v
```

## Check GPU Access in WSL
- Step 1: Open your Ubuntu terminal (WSL)
- Step 2: Run nvidia-smi inside Ubuntu (WSL)
```
nvidia-smi
```

## Create a docker image

 Run the command: 
```
 docker build -t <image name> .
```

Replace <image name> with your desired image name

## Create a Docker container
Run the command: 
```
docker run --gpus all --name <container name> -p 8000:8000 -p 8888:8888 <image name>
```

replace <container name> and <image name> with your container name and image name

## Test import torch and GPU access
```
import torch
print(f"PyTorch version: {torch.__version__}")
print(f"CUDA available: {torch.cuda.is_available()}")
if torch.cuda.is_available():
    print(f"Device: {torch.cuda.get_device_name(0)}")
```







