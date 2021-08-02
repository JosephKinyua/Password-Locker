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