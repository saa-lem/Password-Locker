import unittest
import pyperclip 
from credentials import User
from credentials import Credentials
class TestUser(unittest.TestCase):

    def setUp(self):
        self.new_user = User("Salem", "Owino", "0757871491", "salemowino18@gmail.com", "salem", "leejones2")

    def test_init(self):
        self.assertEqual(self.new_user.first_name,"Salem")
        self.assertEqual(self.new_user.last_name,"Owino")
        self.assertEqual(self.new_user.phone_number,"0757871491")
        self.assertEqual(self.new_user.email_address,"salemowino18@gmail.com")
        self.assertEqual(self.new_user.username, "saa-lem")

