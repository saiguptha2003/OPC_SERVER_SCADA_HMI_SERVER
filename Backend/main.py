from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import time
import threading
from opcua import Client
from fastapi.middleware.cors import CORSMiddleware
import sqlite3
from database import SensorData, initializeDB, storeData,getData
app = FastAPI()

     

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
 


opcua_client = Client("opc.tcp://localhost:4840")

def collectData():
    initializeDB()
    try:
        opcua_client.connect()
        print("Connected to OPC UA Server")

        while True:
            temperature = opcua_client.get_node("ns=2;i=2").get_value()
            pressure = opcua_client.get_node("ns=2;i=3").get_value()
            humidity = opcua_client.get_node("ns=2;i=4").get_value()
            
            sensor_data = SensorData(
                temperature=temperature,
                pressure=pressure,
                humidity=humidity
            )
            storeData(sensor_data)
            print(f"Collected Data - Temperature: {temperature}, Pressure: {pressure}, Humidity: {humidity}")

            time.sleep(1)

    except Exception as e:
        print(f"Error: {e}")
    finally:
        opcua_client.disconnect()
        print("Disconnected from OPC UA Server")
    
threading.Thread(target=collectData, daemon=True).start()

# async def lifespan(app):

#     thread = threading.Thread(target=collectData)
#     thread.daemon = True
#     thread.start()
#     yield
#     print("FastAPI is shutting down.")

@app.get("/sensorData/", response_model=List[SensorData])
async def getSensorData():
    return getData()


#uvicorn main:app --host 0.0.0.0 --port 80