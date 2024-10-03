class SmallCell:
    def __init__(self, max_capacity=16, coverage_area=100):
        self.max_capacity = max_capacity  
        self.coverage_area = coverage_area 
        self.connected_users = []  

    def connect_user(self, user):
        if len(self.connected_users) < self.max_capacity:
            self.connected_users.append(user)
            print(f"User {user.device_id} connected.")
        else:
            print("Small cell at capacity. User cannot connect.")

    def disconnect_user(self, user):
        if user in self.connected_users:
            self.connected_users.remove(user)
            print(f"User {user.device_id} disconnected.")
        else:
            print(f"User {user.device_id} is not connected.")

    def get_connected_users(self):
        return [user.device_id for user in self.connected_users]

    def status(self):
        print(f"Connected users: {len(self.connected_users)}/{self.max_capacity}")
        print(f"Coverage area: {self.coverage_area} meters")

