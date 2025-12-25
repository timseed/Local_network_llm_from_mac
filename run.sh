#!/bin/bash
# On the MAC we SHOULD NOT be running ollama 
echo "Setting Remote OLLAMA Host "
export OLLAMA_HOST="http://192.168.179.130:11434"
echo "Activating python venv 3.10"
source ~/.pe310/bin/activate
nohup streamlit run mychat.py mychat.py --server.address 0.0.0.0 --server.port 8501& 2>&1 >ollama_web.log
echo "Process is running in detached mode"
echo "http://127.0.0.1:8501 to access this"
