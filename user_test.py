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

def test_check_if_userExist(self):

        '''
        A test function to ensure the working of the check if userExist function.
        '''
        self.new_user = User("test","user","0757871491","salemowino18@gmail.com","sa-lem","leejones1")
        self.new_user.save_userDetails()

        user2 = User("test","user","0757871491","salemowino@gmail.com","sa-lem","leejones1")

        for user in User.users_list:
            if user.username == user2.username and user.password == user2.password:
                current_user = user.first_name
        return current_user
        '''
        A test function to ensure the working of the check if userExist function.
        '''
        self.new_user = User("test","user","0757871491","salemowino18@gmail.com","saa-lem","leejones1")
        self.new_user.save_userDetails()

        user2 = User("test","user","0757871491","salemowino18@gmail.com","saa-lem","leejones1")

        for user in User.users_list:
            if user.username == user2.username and user.password == user2.password:
                current_user = user.first_name
        return current_user
        test_user.save_userDetails()
        self.assertEqual(len(User.users_list),2)
def test_check_if_userExist(self):

        '''
        A test function to ensure the working of the check if userExist function.
        '''
        self.new_user = User("test","user","0780404626","helloemryon@gmail.com","Pwamaria","leejones1")
        self.new_user.save_userDetails()

        user2 = User("test","user","0780404626","helloemryon@gmail.com","Pwamaria","leejones1")

        for user in User.users_list:
            if user.username == user2.username and user.password == user2.password:
                current_user = user.first_name
        return current_user
        '''
        A test function to ensure the working of the check if userExist function.
        '''
        self.new_user = User("test","user","0780404626","helloemryon@gmail.com","Pwamaria","leejones1")
        self.new_user.save_userDetails()

        user2 = User("test","user","0780404626","helloemryon@gmail.com","Pwamaria","leejones1")

        for user in User.users_list:
            if user.username == user2.username and user.password == user2.password:
                current_user = user.first_name
        return current_user
        test_user.save_userDetails()
        self.assertEqual(len(User.users_list),2)


 def tearDown(self):
        '''
        A funtcion to clear the credential list after every test
        '''
        
        Credentials.credentials_list = []
        User.users_list = []