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
        self.new_user = User("test","user","0757871491","salemowino18@gmail.com","saalem","leejones1")
        self.new_user.save_userDetails()

        user2 = User("test","user","0757871491","salemowino18@gmail.com","saalem","leejones1")

        for user in User.users_list:
            if user.username == user2.username and user.password == user2.password:
                current_user = user.first_name
        return current_user
        '''
        A test function to ensure the working of the check if userExist function.
        '''
        self.new_user = User("test","user","0757871491","salemowino18@gmail.com","saalem","leejones1")
        self.new_user.save_userDetails()

        user2 = User("test","user","0757871491","salemowino18@gmail.com","saalem","leejones1")

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


         def test_save_credentials(self):

        '''
        A funtion to check if the method save_credentials is saving the new credenntials as expected.
        '''
        
        self.new_credential.save_credentials()
        twitter = Credentials("twitter", "Just Salem","@salemitho", "salemowino18@gmail.com","leejones1" )
        twitter.save_credentials()

        self.assertEqual(len(Credentials.credentials_list), 2)


    def test_delete_credentials(self):

        self.new_credential.save_credentials()
        twitter = Credentials("twitter", "Just Salem","@salemitho", "salemowino18@gmail.com","leejones1" )
        twitter.save_credentials()
        self.new_credential.delete_credentials()
        self.assertEqual(len(Credentials.credentials_list),1)



def test_display_credentials(self):
        
        '''
        A funtion to test if we are able to display the right credentials
        '''
        self.new_credential.save_credentials()
        twitter = Credentials("twitter", "salemitho","@salemmatico", "salemowino18@gmail.com","leejones1" )
        twitter.save_credentials()
        google = Credentials("google", "Salem Owino","Saa-lem", "salemowino18@gmail.com","leejones2" )
        google.save_credentials()

        self.assertEqual(len(Credentials.display_credentials(google.username)),1)


    def test_find_by_account_type(self):
        '''
        Test to check if the find_by_account_type method returns the correct credential
        '''
        self.new_credential.save_credentials()
        google = Credentials("google", "Salem Owino","Saa-lem", "salemowino18@gmail.com","leejones2" )
        google.save_credentials()
        credential_found = Credentials.find_by_account_type('google')
        self.assertEqual(credential_found,google)

         def test_copy_credentials(self):
        '''
        A funtcion to test to check if the copy a credential method copies the correct credential
        '''
        self.new_credential.save_credentials()
        google = Credentials("google", "Salem Owino","salemitho", "salemowino18@gmail.com","leejones2" )
        google.save_credentials()
        found_credential = None
        for credential in Credentials.user_credentials_list:
                found_credential = Credentials.find_by_account_type(credential.account_type)
                return pyperclip.copy(found_credential.account_password)
        Credentials.copy_credentials(self.new_credential.account_type)
        self.assertEqual('leejones2', pyperclip.paste())
        print(pyperclip.paste())





if __name__=='__main__':
  unittest.main()