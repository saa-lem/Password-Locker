import unittest
from user import User

class TestUser(unittest.TestCase):
    
    '''
     Test clas that  defines test cases foe the User class
    '''

    def setUp(self):

        '''
        Method to run before test cases
        '''
        self.new_user = User('Salem', 'Owino', 'Salemitho', 'steph1')

    def test_init(self):

        '''
        Test case to check if initialization of objects are proper
        '''

        self.assertEqual(self.new_user.first_name, 'Salem')

        self.assertEqual(self.new_user.last_name, 'Owino')

        self.assertEqual(self.new_user.username, 'Salemitho')

        self.assertEqual(self.new_user.password, 'steph1')

    def test_save_user(self):

        '''
        Test case to check if the users info can be saved
        '''
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)

    def test_user_exists(self):
        
        '''
        Test case to check if the users info already exisits
        '''
        self.new_user.save_user()
        self.assertTrue(User.user_exists('Salemitho'))



if __name__ == '__main__':
    unittest.main()
