@echo off
REM Create and activate the virtual environment
python -m venv OPC_SERVER_SCADA_ENV
call OPC_SERVER_SCADA_ENV\Scripts\activate

REM Install requirements
pip install -r Backend\requirements.txt

REM Start FastAPI Server
echo Starting FastAPI server...
cd Backend
start /B uvicorn main:app

REM Start React Server
echo Starting React server...
cd ..\scada_frontend
npm install  REM Ensure all Node dependencies are installed
start /B npm start

REM Start OPC Server
echo Starting OPC server...
cd ..\opc_server  REM Update to your actual OPC server path if necessary
start /B python OPCServer.py

REM Wait for all servers to start (Optional - can be used to wait for user input)
echo All servers are up and running. Press any key to exit...
pause
