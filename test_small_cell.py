import unittest
from src.small_cell import SmallCell
from src.user_device import UserDevice

class TestSmallCell(unittest.TestCase):
    def test_connect_user(self):
        small_cell = SmallCell(max_capacity=2)
        user1 = UserDevice("TestDevice001", location=50)
        user2 = UserDevice("TestDevice002", location=30)

        user1.connect_to_cell(small_cell)
        user2.connect_to_cell(small_cell)

        self.assertEqual(len(small_cell.get_connected_users()), 2)

        user3 = UserDevice("TestDevice003", location=20)
        user3.connect_to_cell(small_cell)
        self.assertEqual(len(small_cell.get_connected_users()), 2)  

if __name__ == "__main__":
    unittest.main()
