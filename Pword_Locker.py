#!/usr/bin/env python3.6
import pyperclip
import string
import secrets
import random
from credentials import Credentials
from credentials import User

#Create a new user
def create_user(f_name, l_name, p_number, e_address, u_name, p_word):
    '''
    A funtcion to create a new user.
    '''
    new_user = User(f_name, l_name, p_number, e_address, u_name, p_word)
    
    return new_user


#Create new credentials
def create_credentials(at_type, at_rname, at_remail, at_uname, at_password):
    '''
    A funtion to create new credentials.
    '''
    new_credential = Credentials(at_type, at_rname, at_remail, at_uname, at_password)
    return new_credential

#save user
def save_userDetails(new_user):
    '''
    a funtion to save user details
    '''
    User.save_userDetails(new_user)

def save_credentials(new_credential):
    '''
    A funtion to save credentials.
    '''
    Credentials.save_credentials(new_credential)


#delete credentials
def delete_credentials(credential):
    '''
    A funtcion to delete a given credentials.
    '''
    Credentials.delete_credentials(credential)


def check_if_userExist(uname, pword):
    '''
    A function to return the user associated with the give password and username.
    '''
    return Credentials.check_if_userExist(uname, pword)

def generate_pword(pword_length):
    '''
    A funtion to generate password, combining random letters and digits
    '''
    return Credentials.generate_password(pword_length)

@classmethod
def display_credentials(cls,uname):
    '''
    A class method that displays all credentials of a given username.
    '''

    return Credentials.display_credentials(cls, uname)


@classmethod
def find_by_account_type(cls, account_site):
    '''
    A function to search for credentials when given an account site search as google, or twitter.
    '''
    return cls.find_by_account_type(cls, account_type)

@classmethod
def copy_credentials(cls, account_site):
    '''
    A class method to enable us to copy credentials of a given site name.
    '''
    return cls.copy_credentials(cls, account_site)

#main method
    main()





    © 2020 GitHub, Inc.
    Terms
    Privacy
    Security
    Status
    Help

Contact GitHub
Pricing
API
Training
Blog

def main():
    print('\n')
    print("            *  *          *  *          ")
    print("          *      *      *      *        ")
    print("         *         *  *         *       ")
    print("         *       WELCOME        *       ")
    print("         *         TO           *       ")
    print("          *      PASSWORD      *        ")
    print("           *      LOCKER      *         ")
    print("            *                *          ")
    print("              *            *            ")
    print("                *        *              ")
    print("                   *  *                 ")
    print('\n')
    guest_name = input("What is your name please?")
    print('\n')

    print(f"Hello {guest_name}, welcome to Password Locker:")
    print('\n')
    while True:
        print('\n')
        print(r"*"*30)
        print('\n')
        print("Use these short codes to navigate through Password_Locker:\n ln to log in \n ca to create a new account. \n ex to exit" )
        print('\n')
        
        short_code = input().lower()
        if short_code == 'ca':
            print("New Account")
            print("-"*10)

            print("Enter First Name ...")
            f_name = input()

            print("Enter Last Name ...")
            l_name = input()

            print("Enter Phone Number ...")
            p_number = input()

            print(" Enter Email Address ...")
            e_address = input()

            print("Enter your prefferred username ...")
            u_name = input()

            # p_word = input("Enter a password you can remember")

            

            print("Do you want to input your own password or have one generated for you? Use short codes\n'gp\' to generate password.\n \'cyo\' to choose your own password \n \'ex\' to exit... ")
            password_choice = input()
            p_word = ''
           
            if password_choice == 'cyo':
                p_word = p_word.join(input("Enter a password of your choice..."))
                # break

            elif password_choice == 'gp':
                print("Enter the length of the password you wish to generate eg 9 ")
                p_length = input()
                p_word = p_word.join(Credentials.generate_password(p_length))
                # break

            elif password_choice == 'ex':
                break

            else: 
                print("Sorry I didn\'t get that. Please try again")


         

            save_userDetails(create_user(f_name, l_name, p_number, e_address,u_name, p_word))#Create and save new user
            print('\n')
            print(f"New Account for {f_name} {l_name} created.")
            print('\n')
            print(f"Your password is {p_word} :-Use it to log in using short code ln")

            print('\n')

        elif short_code == 'ln':
            print('\n')
            print("Enter your account details to log in: \n Enter your username...")
            u_name = input()
            print("Enter your password...")
            p_word = input()
            account_exist = check_if_userExist(u_name, p_word)
            if account_exist == u_name:
                print('\n')
                print(f"Welcome to your Password locker account {u_name}: \n Please choose an option to continue...")
                print('\n')
                while True:
                    print('\n')
                    print("Navigation short codes: \n cc to create new credentials: \n dc to display credentials: \n sc to search credentials: \n rm to remove or delete credentials: \n copy to copy credentials: \n ex to exit")
                    print('\n')
                    short_code = input().lower()
                    if short_code == 'cc':
                        print('\n')
                        print("Enter your credential details")
                        print("Enter account type... eg \'google\'")
                        at_type = input()
                        print(f"Enter the full name you used or you wish to use to register with {at_type}")
                        at_rname = input()
                        print(f"Enter the email you used or you wish to use to register with {at_type}")
                        at_remail = input()
                        print(f"Enter the username you used or would love to use on {at_type}")
                        at_uname = input()

                        while True:
                            print("Do you want to input your own password or have one generated for you? Use short codes\n'gp\' to generate password.\n \'cyo\' to choose your own password \n \'ex\' to exit... ")
                            password_choice = input()
                            if password_choice == 'cyo':
                                at_password = input("Enter a password of your choice...")
                                break

                            elif password_choice == 'gp':
                                print("Enter the length of the password you wish to generate eg 9 ")
                                p_length = input()
                                p_length = int(p_length)
                                at_password = Credentials.generate_password(p_length)
                                break

                            elif password_choice == 'ex':
                                break

                            else: 
                                print("Sorry I didn\'t get that. Please try again")


                        # return at_password

                        save_credentials(create_credentials(at_type, at_rname, at_remail, at_uname, at_password))
                        print(' \n')
                        print(f'Credential Created:\n Account type: {at_type} \n Account Registration Name: {at_rname}\n Account registration Email: {at_remail} \n Account Username: {at_uname} \n Account Password: {at_password}')
                        print('\n ')

                    elif short_code == 'dc':
                        if display_credentials(u_name):
                            print("Here is a list of your credentials:")
                            print('\n')
                            for credential in display_credentials(u_name):
                                print(f"Credential Created:\n Account type: {at_type} \n Account Registration Name: {at_rname}\n Account registration Email: {at_remail} \n Account Username: {at_uname} \n Account Password: {at_password}")

                        else:
                            print("You don\'t have any credentials yet")

                    elif short_code == 'rm':
                        print("Enter the account type of the credential you wish to delete:...")
                        credential_to_delete = input()
                        if find_by_account_type(credential_to_delete):
                            credential_to_delete = delete_credentials(credential_to_delete)
                            print("Credential successfully deleted!")
                        else:
                            print(" We couldin\'t find the credentials associated with the account name you typed.")

                    elif short_code == "copy":
                        print(' \n')
                        account_of_interrest = input('Enter the account type for the credential password to copy: ')
                        copy_credentials(account_of_interrest)
                        print('\n')

                    else:
                        print("I didn\'t get that, please try again")

            else:
                print(f"Sorry, we couldn\'t' find any account under the name {u_name}")    
                print('\n')        
        elif short_code == 'ex':
            break

        else:
            print("I really did'nt get that, please use the short code ")
print('\n')

if __name__=='__main__':
    main()