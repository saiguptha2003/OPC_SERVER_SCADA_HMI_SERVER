# OPC SERVER WITH WEB-BASED SCADA HMI (HUMAN MECHINE INTERFACE)


## Manual INSTALLATION OF REQUIRED MODULES IN THE SYSTEMS

```pip
python -m venv OPC_SERVER_SCADA_ENV
```
### create the virtual python environment for this project

```python
cd SCADA_OPC_SERVER
OPC_SERVER_SCADA_ENV\Scripts\activate
```
### Execute the above command to start virtual environment 


```python
pip install -r requirements.txt

```
### Execute the above command to install all dependencies for this project


```bash
python OPCServer.py 
```
#### Execute the above command to start the OPC-UA SERVER 

```bash
cd Backend
uvicorn main:app 
```
#### Execute the abobve command to start the fastapi Backend Server

```bash
cd ..
cd scada_frontend
npm install
```
#### Execute the above command to install required dependencies for frontend application

```bash
npm start
```
#### Execute the above command to start the frontend server 

## Automatic Installation through Scripts 

#### Start the servers using bash script (Linux Based Systems)


```bash

chmod +x startup.sh

```
##### enable the execution permission
```bash
./startup.sh
```

#### Start the servers using Batch script (Windows Based Systems)

```batch
startup.bat
```


## Work Flow

1. Start
2. Start the OPC Server which generates the data and Publish the Data
3. Start the FastAPI Server which acts as OPC Client And consumes data 
4. Start the FrontEND application to visualize the data fecting from the OPC SERVER
5. Stop Server

## For Results Please REFER RESULTS Folder