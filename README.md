# Deploy-Model-on-local-server
## Install Ubuntu in WSL
1 
## Check the GPU

PS C:\Users\PLS_2> Get-CimInstance Win32_VideoController | Select-Object Name, DriverVersion, AdapterRAM

Name                                   DriverVersion AdapterRAM
----                                   ------------- ----------
NVIDIA GeForce RTX 3050 6GB Laptop GPU 32.0.15.6078  4293918720
Intel(R) Iris(R) Xe Graphics           32.0.101.5763 2147479552


PS C:\Users\PLS_2> nvidia-smi
Fri Jun  6 12:17:50 2025
+-----------------------------------------------------------------------------------------+
| NVIDIA-SMI 560.78                 Driver Version: 560.78         CUDA Version: 12.6     |
|-----------------------------------------+------------------------+----------------------+
| GPU  Name                  Driver-Model | Bus-Id          Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |
|                                         |                        |               MIG M. |
|=========================================+========================+======================|
|   0  NVIDIA GeForce RTX 3050 ...  WDDM  |   00000000:01:00.0 Off |                  N/A |
| N/A   51C    P5              7W /   60W |     561MiB /   6144MiB |     65%      Default |
|                                         |                        |                  N/A |
+-----------------------------------------+------------------------+----------------------+

+-----------------------------------------------------------------------------------------+
| Processes:                                                                              |
|  GPU   GI   CI        PID   Type   Process name                              GPU Memory |
|        ID   ID                                                               Usage      |
|=========================================================================================|
|    0   N/A  N/A     22372    C+G   ...iles\obs-studio\bin\64bit\obs64.exe      N/A      |
+-----------------------------------------------------------------------------------------+
PS C:\Users\PLS_2> exit



