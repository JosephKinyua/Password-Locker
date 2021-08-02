#!/usr/bin/env python3.8.10

import random
from user import User
from credentials import Credentials
import string

# Functions to add credentials
def create_new_credential(account_name, account_password):
    """Function to create a new account and its credentials"""
    new_credential = Credentials(account_name, account_password)
    return new_credential

def save_new_credential(credentials):
    """Function to save the newly created account and password"""
    credentials.save_credentials()


def find_credential(account_name):
    """Function that finds credentials based on account_name given"""
    return Credentials.find_by_name(account_name)

def find_credential(account_name):
    """Function that finds credentials based on account_name given"""
    return Credentials.find_by_name(account_name)


def check_existing_credentials(name):
    """Method that checks whether a particular account and its credentials exist based on searched account_name"""
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
        print("Use  short codes to select an option: Create New User use 'cu': Login to your account use 'lg' or 'ex' to exit password locker")
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