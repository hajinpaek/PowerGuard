class Backhaul:
    def __init__(self, connection_type="fiber", bandwidth=100):
        self.connection_type = connection_type 
        self.bandwidth = bandwidth  

    def status(self):
        print(f"Backhaul type: {self.connection_type}")
        print(f"Bandwidth: {self.bandwidth} Mbps")

    def change_type(self, new_type, new_bandwidth):
        self.connection_type = new_type
        self.bandwidth = new_bandwidth
        print(f"Backhaul updated to {new_type} with {new_bandwidth} Mbps")

