from opcua import Server
from opcua import ua
import time
import random
from datetime import datetime

class HistoricalData:
    def __init__(self):
        self.data = []  

    def addReading(self, timestamp, temperature, pressure):
        self.data.append((timestamp, temperature, pressure))

    def getHistory(self):
        return self.data

server = Server()
server.set_endpoint("opc.tcp://localhost:4840")
server.set_server_name("Python OPC UA Server")
namespace = server.register_namespace("http://Leucine.io.server")
objects = server.get_objects_node()
myFolder = objects.add_folder(namespace, "MySensorData")
temperatureNode = myFolder.add_variable(namespace, "Temperature", 0.0)
pressureNode = myFolder.add_variable(namespace, "Pressure", 0.0)
humidityNode = myFolder.add_variable(namespace, "Humidity", 0.0)
temperatureNode.set_writable()
pressureNode.set_writable()
humidityNode.set_writable()


historicalData = HistoricalData()

def get_historical_data():
    history = historicalData.get_history()
    return history

historical_data_method = myFolder.add_method(namespace, "GetHistoricalData", get_historical_data, [], [ua.VariantType.String])

server.start()
print("OPC UA Server is running at opc.tcp://localhost:4840")

try:
    while True:
        temperature = random.uniform(10.0, 50.0)
        pressure = random.uniform(1.0, 20.0)
        temperatureNode.set_value(temperature)
        pressureNode.set_value(pressure)
        
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        historicalData.addReading(timestamp, temperature, pressure)

        print(f"Temperature: {temperature} °C, Pressure: {pressure} bar at {timestamp}")

        time.sleep(1)

except KeyboardInterrupt:
    print("Shutting down OPC UA Server...")

finally:
    print(historicalData.getHistory())
    server.stop()
    print("Server stopped.")
