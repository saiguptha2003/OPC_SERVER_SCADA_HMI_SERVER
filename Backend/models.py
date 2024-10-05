from pydantic import BaseModel
class SensorData(BaseModel):
    temperature: float  
    pressure: float     
    humidity: float    