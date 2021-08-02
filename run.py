#!/usr/bin/env python3.6

import random
from user import User
from credentials import Credentials
import string

# Functions to add credentials


def create_new_credential(account_name, account_password):
    """
    
    Function to create a new account and its credentials
    
    """
    new_credential = Credentials(account_name, account_password)
    return new_credential


def save_new_credential(credentials):
    """
    
    Function to save the newly created account and password
    
    """
    credentials.save_credentials()


def find_credential(account_name):
    """
    
    Function that finds credentials based on account_name given
    
    """
    return Credentials.find_by_name(account_name)


def check_existing_credentials(name):
    """
    
    Checks whether a particular account and its credentials exist based on searched account_name
    
    """
    return Credentials.find_by_name(name)


def display_credentials():
    """Function which displays all saved credentials"""
    return Credentials.display_credentials()


def delete_credential(credentials):
    """
    Method that deletes credentials
    """
    return Credentials.delete_credential(credentials)


def main():

    while True:
        print('''

             Welcome to Password Locker
    An Easy and Simple Application for Storing your 
             Password  Locally Via Terminal

  ''')
        print('\n')
        print("Select an option using short codes: Create New User use 'cu': Login to your account use 'lg' or 'ex' to exit password locker")
        short_code = input().lower()
        print('\n')

        if short_code == 'cu':
            print("Create a UserName")
            created_user_name = input()

            print("Enter Password")
            created_user_password = input()

            print("Confirm  Password")
            confirm_password = input()

            while confirm_password != created_user_password:
                print("Sorry your passwords did not match!")
                print("Please enter the correct password")
                created_user_password = input()
                print("Confirm Your Password")
                confirm_password = input()
            else:
                print(f"Congratulations! {created_user_name}! You have created your new account.")
                print('\n')
                print("Proceed to Log In to your Account")
                print("Username")
                entered_userName = input()
                print("Your Password")
                entered_password = input()

                while entered_userName != created_user_name or entered_password != created_user_password:
                    print("Wrong username or password")
                    print("Username")
                    entered_userName = input()
                    print("Your Password")
                    entered_password = input()
                else:
                    print(f"Welcome!: {entered_userName} to your Account")
                    print('\n')

                    print("Select an option below to continue: Enter sc, ac, dc, sc or lo")
                    print('\n')

                while True:
                    print("sc: Saved credentials")
                    print("ac: Add new credentials")
                    print("dc: Delete credentials")
                    print("sc: Search credentials")
                    print("lo: Log Out")
                    option = input()

                    if option == 'ac':
                        while True:
                            print("Continue to add? y/n")

                            choice = input().lower()
                            if choice == 'y':
                                print("Enter The Account Name")
                                account_name = input()
                                print("Enter a password")
                                print(
                                    "To generate random password enter keyword 'gp' or 'n' to create your own password")
                                keyword = input().lower()
                                if keyword == 'gp':
                                    source = string.ascii_letters + string.digits
                                    account_password = ''.join((random.choice(source) for i in range(8)))
                                    print(f"Account: {account_name}")
                                    print(f"Password: {account_password}")
                                    print('\n')
                                elif keyword == 'n':
                                    print("Create your password")
                                    account_password = input()
                                    print(f"Account: {account_name}")
                                    print(f"Password: {account_password}")
                                    print('\n')

                                else:
                                    print("Please enter a valid Code")

                                save_new_credential(create_new_credential(account_name, account_password))
                            elif choice == 'n':
                                break
                            else:
                                print("Please use 'y' for yes or 'n' for no!")
                    elif option == 'sc':
                        while True:
                            print("Below is a list of all your credentials")
                            if display_credentials():

                                for credential in display_credentials():
                                    print(f"Account Name:{credential.account_name}")
                                    print(f"Password:{credential.account_password}")

                            else:
                                print('\n')
                                print("You don't  have any contacts yet")
                                print('\n')

                            print("Back to Menu? y/n")

                            back = input().lower()
                            if back == 'y':
                                break
                            elif back == 'n':
                                continue
                            else:
                                print("Please Enter a valid code")
                                continue

                    elif option == 'lo':
                        print("Warning! You will loose all your credentials if you log out. Are you sure? y/n")
                        logout = input().lower()

                        if logout == 'y':
                            print("You have Successfully logged out")
                            break
                        elif logout == 'n':
                            continue
                    elif option == 'dc':
                        while True:
                            print("Search for credential to delete")

                            search_name = input()

                            if check_existing_credentials(search_name):
                                search_credential = find_credential(search_name)
                                print(f"Account Name: {search_credential.account_name} \n Password: {search_credential.account_password}")
                                print("Delete? y/n")
                                sure = input().lower()
                                if sure == 'y':
                                    delete_credential(search_credential)
                                    print("Account successfully deleted")
                                    break
                                elif sure == 'n':
                                    continue

                            else:
                                print("That Contact Does not exist")
                                break

                    elif option == 'sc':
                        while True:
                            print("Continue? y/n")
                            option2 = input().lower()
                            if option2 == 'y':
                                print("Enter an account name to find credentials")

                                search_name = input()

                                if check_existing_credentials(search_name):
                                    search_credential = find_credential(search_name)
                                    print(f"Account Name: {search_credential.account_name} \n Password: {search_credential.account_password}")
                                else:
                                    print("That Contact Does not exist")
                            elif option2 == 'n':
                                break
                            else:
                                print("Please enter a valid code")

                    else:
                        print("Please enter a valid code")
                        continue

        elif short_code == 'lg':
            print("WELCOME")
            print("Enter UserName")
            default_user_name = input()

            print("Enter Your password")
            default_user_password = input()
            print('\n')

            while default_user_name != 'testuser' or default_user_password != '12345':
                print("Wrong userName or password. Username 'testuser' and password '12345'")
                print("Enter UserName")
                default_user_name = input()

                print("Enter Your password")
                default_user_password = input()

                print('\n')

            if default_user_name == 'testuser' and default_user_password == '12345':
                print("You have successfully signed up!")
                print('\n')
                print("Select an option below to continue: Enter sc, ac, dc, sc or lo")
                print('\n')

            while True:
                print("sc: View Your saved credentials")
                print("ac: Add new credentials")
                print("dc: Delete credentials")
                print("sc: Search credentials")
                print("lo: Log Out")
                option = input()

                if option == 'ac':
                    while True:
                        print("Continue to add? y/n")

                        choice = input().lower()
                        if choice == 'y':
                            print("Enter The Account Name")
                            account_name = input()
                            print("Enter a password")
                            print(
                                "To generate random password enter keyword 'gp' or 'n' to create your own password")
                            keyword = input().lower()
                            if keyword == 'gp':
                                source = string.ascii_letters + string.digits
                                account_password = ''.join((random.choice(source) for i in range(8)))
                                print(f"Account: {account_name}")
                                print(f"Password: {account_password}")
                                print('\n')
                            elif keyword == 'n':
                                print("Create your password")
                                account_password = input()
                                print(f"Account: {account_name}")
                                print(f"Password: {account_password}")
                                print('\n')

                            else:
                                print("Please enter a valid Code")

                            save_new_credential(create_new_credential(
                                account_name, account_password))
                        elif choice == 'n':
                            break
                        else:
                            print("Please use 'y' for yes or 'n' for no!")
                elif option == 'sc':
                    while True:
                        print("Below is a list of all your credentials")
                        if display_credentials():

                            for credential in display_credentials():
                                print(f"ACCOUNT NAME:{credential.account_name}")
                                print(f"PASSWORD:{credential.account_password}")

                        else:
                            print('\n')
                            print("You don't seem to have any contacts yet")
                            print('\n')

                        print("Back to Menu? y/n")

                        back = input().lower()
                        if back == 'y':
                            break
                        elif back == 'n':
                            continue
                        else:
                            print("Please Enter a valid code")
                    
                elif option == 'lo':
                    print("Warning! You will loose all your credentials if you log out. Are you sure? y/n")
                    logout = input().lower()

                    if logout == 'y':
                        print("You have Successfully logged out")
                        break
                    elif logout == 'n':
                        continue

                elif option == 'dc':
                    while True:
                        print("Search for credential to delete")

                        search_name = input()

                        if check_existing_credentials(search_name):
                            search_credential = find_credential(search_name)
                            print(f"Account Name: {search_credential.account_name} \n PASSWORD: {search_credential.account_password}")
                            print("Delete? y/n")
                            sure = input().lower()
                            if sure == 'y':
                                delete_credential(search_credential)
                                print("Account succefully deleted!")
                                break
                            elif sure == 'n':
                                continue

                        else:
                            print("That Contact Does not exist")
                            break

                elif option == 'sc':
                    while True:
                        print("Continue? y/n")
                        option2 = input().lower()
                        if option2 == 'y':
                            print("Enter an account name to find credentials")

                            search_name = input()

                            if check_existing_credentials(search_name):
                                search_credential = find_credential(search_name)
                                print(f"Account Name: {search_credential.account_name} \n Password: {search_credential.account_password}")
                            else:
                                print("That Contact Does not exist")
                        elif option2 == 'n':
                            break
                        else:
                            print("Please enter a valid code")
                else:
                    print("Please enter a valid code")
        elif short_code == 'ex':
            break
        else:
            print("Please Enter a valid code to continue")


if __name__ == '__main__':
    main()
