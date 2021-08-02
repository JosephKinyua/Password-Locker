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