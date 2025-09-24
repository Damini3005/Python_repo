import json
import logging

logging.basicConfig(level=logging.INFO)
# (Assume the Server class is defined here)
class Server:
    def __init__(self, hostname: str, ip_address: str, status: str, cpu_usage: float, memory_usage: float):
        self.hostname = hostname
        self.ip_address = ip_address
        self.status = status
        self.cpu_usage = cpu_usage
        self.memory_usage = memory_usage
        
    def __repr__(self):
        return (f"Server(hostname='{self.hostname}', ip='{self.ip_address}', "
                f"status='{self.status}', cpu={self.cpu_usage}%, mem={self.memory_usage}%)")

all_servers = []
with open("datacenters.json", 'r') as file:
    data = json.load(file)

  
    for dc in data["datacenters"]:
        dc_name = dc["name"]
       
        for server_data in dc["servers"]:
            
            server_obj = Server(
                hostname=server_data["hostname"],
                ip_address=server_data["ip"],
                status=server_data["status"],
                cpu_usage=float(server_data["cpu"]),
                memory_usage=float(server_data["mem"])
            )
            all_servers.append(server_obj)

print("--- All Servers Loaded from Nested JSON ---")
for server in all_servers:
    logging.info(server)