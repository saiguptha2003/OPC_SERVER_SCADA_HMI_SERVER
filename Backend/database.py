import sqlite3
from typing import List
from pydantic import BaseModel


class SensorData(BaseModel):
    temperature: float
    pressure: float
    humidity: float

DATABASE = 'SCADA_OPC.db'

def initializeDB():
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS SensorData (id INTEGER PRIMARY KEY AUTOINCREMENT,temperature REAL,pressure REAL,humidity REAL,timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)
        ''')
        conn.commit()

def storeData(data: SensorData):
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO SensorData (temperature, pressure, humidity)
            VALUES (?, ?, ?)
        ''', (data.temperature, data.pressure, data.humidity))
        conn.commit()

def getData() -> List[SensorData]:
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT temperature, pressure, humidity FROM sensorData')
        rows = cursor.fetchall()
        return [SensorData(temperature=row[0], pressure=row[1], humidity=row[2]) for row in rows]