from small_cell import SmallCell
from user_device import UserDevice
from backhaul import Backhaul

small_cell = SmallCell(max_capacity=10, coverage_area=150)

backhaul = Backhaul()

user1 = UserDevice("Device001", location=50)
user2 = UserDevice("Device002", location=160) 
user3 = UserDevice("Device003", location=90)

user1.connect_to_cell(small_cell)
user2.connect_to_cell(small_cell)
user3.connect_to_cell(small_cell)

small_cell.status()

backhaul.status()

backhaul.change_type("satellite", 20)

user1.disconnect_from_cell(small_cell)

small_cell.status()
