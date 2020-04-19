import pyperclip
import string
import secrets

class User:
    users_list = []
    def __init__(self, first_name, last_name, phone_number, email_address, username, password):

        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email_address = email_address
        self.username = username
        self.password = password

    def save_userDetails(self):
        '''
        A funtction to save the new user to the user list.
        '''
        User.users_list.append(self)


    def delete_userDetails(self):
        '''
        A function to delete a specific user.
        '''
        User.users_list.remove(self)


class Credentials:

    '''
    A class to hold the user's credentials, genrate passwords and also store the information
    '''
    
    credentials_list = []
    user_credentials_list = []
    def __init__(self, account_type,registration_name, username, registration_email, account_password):
        self.account_type = account_type
        self.registration_name = registration_name
        self.username = username
        self.registration_email = registration_email
        self.account_password = account_password

    @classmethod
    def check_if_userExist(cls,userName,password):

        '''
        A method to check if the user with the entered credentials exist
        '''

        current_user = " "
        for user in User.users_list:
            if user.username == userName and user.password == password:
                current_user = user.username
        return current_user


    # def save_user(self):
    #     '''
    #     A funtction to save the new user to the user list.
    #     '''
    #     User.user_list.append(self)



    def save_credentials(self):
        '''
        Function to save a newly created user credentials
        '''
    
        Credentials.credentials_list.append(self)

    def delete_credentials(self):
        '''
        A function to delete credentials.
        '''
        Credentials.credentials_list.remove(self)



    def generate_password(string_length = 9):
        '''
        Generate a secure password using letters and numbers.
        '''
        password_characters = string.ascii_letters + string.digits

        return ''.join(secrets.choice(password_characters) for i in range(int(string_length)))
        # print("Your generated password is ", generate_password() )


    @classmethod
    def display_credentials(cls,username):
        '''
        A method to display credentials  depending on the input username.
        '''
        user_credentials_list = []
        for credential in cls.credentials_list:
            if credential.username == username:
                user_credentials_list.append(credential)
        return user_credentials_list

    @classmethod
    def find_by_account_type(cls, account_site):
        '''
        A method to search for credentials associated with a given account type.
        '''
        for credential in cls.credentials_list:
            if credential.account_type == account_site:

                return credential


    @classmethod
    def copy_credentials(cls,account_site):
        '''
        Class method that copies a credential's info after the credential's account site is entered
        '''
        found_credential = cls.find_by_account_type(account_site)
        return pyperclip.copy(found_credential.account_password)

        


    