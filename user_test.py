import unittest
import pyperclip 
from credentials import User
from credentials import Credentials
class TestUser(unittest.TestCase):

    def setUp(self):
        self.new_user = User("Salem", "Owino", "0757871491", "salemowino18@gmail.com", "saa-lem", "leejones2")

    def test_init(self):
        self.assertEqual(self.new_user.first_name,"Salem")
        self.assertEqual(self.new_user.last_name,"Owino")
        self.assertEqual(self.new_user.phone_number,"0757871491")
        self.assertEqual(self.new_user.email_address,"salemowino18@gmail.com")
        self.assertEqual(self.new_user.username, "saa-lem")
        self.assertEqual(self.new_user.password, "leejones1")



    def tearDown(self):
                
        credentials_list = []
        User.users_list = []


    def test_save_multiple_userDetails(self):
        self.new_user.save_userDetails()
        test_user = User("test","user","0757871491","salemowino18@gmail.com","saa-lem","leejones")
        test_user.save_userDetails()
        self.assertEqual(len(User.users_list),2)


 def test_delete_userDetails(self):
        '''
        A function to test if we are able to delete user details.
        '''

        self.new_user.save_userDetails()
        test_user = User("test","user","0757871491","salemowino18@gmail.com","saa-lem","leejones")
        test_user.save_userDetails()

        self.new_user.delete_userDetails()
        self.assertEqual(len(User.users_list),1)
