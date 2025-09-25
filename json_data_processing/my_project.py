import json
# (Assume the Server class is defined here)
class Server:
    def __init__(self, hostname: str, ip_address: str, status: str, cpu_usage: float, memory_usage: float):
        self.hostname     = hostname
        self.ip_address   = ip_address
        self.status       = status
        self.cpu_usage    = cpu_usage
        self.memory_usage = memory_usage
        
    def __repr__(self):
        return (f"Server(hostname='{self.hostname}', ip='{self.ip_address}', "
                f"status='{self.status}', cpu={self.cpu_usage}%, mem={self.memory_usage}%)")

with open("datacenters.json", 'r') as txt:
    data = json.load(txt)

all_server = []
print(type(data))
for i, j in data.items():
    k = 1
    for n in j:
        print(n['name'])
        for l in n['servers']:
            print(l)
            obj = Server(l['hostname'], l['ip'], l['status'], l['cpu'], l['mem'])
            all_server.append(obj)
        print(25*"_")    

print(all_server)

for obje in all_server:
    print(obje)    


