#!/bin/bash

# Create and activate the virtual environment 
python -m venv OPC_SERVER_SCADA_ENV
echo "Activating FastAPI virtual environment..."
source OPC_SERVER_SCADA_ENV/bin/activate  # Update this path if necessary

# Install requirements
pip install -r Backend/requirements.txt

# Start FastAPI Server
echo "Starting FastAPI server..."
cd Backend
uvicorn main:app &

# Start React Server
echo "Starting React server..."
cd ../scada_frontend
npm install  # Ensure all Node dependencies are installed
npm start &

# Start OPC Server
echo "Starting OPC server..."
cd ../opc_server  # Update to your actual OPC server path if necessary
python OPCServer.py &

# Wait for all servers to start
wait

echo "All servers are up and running."
