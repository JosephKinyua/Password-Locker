import unittest
from credentials import Credentials

class TestCredentials(unittest.TestCase):
    """
    Test class that defines test cases for the Credentials class behavior
    """
    def setUp(self):
            """
            Set up method to run  before each test case
            
            """
    self.new_credentials = Credentials("Facebook", "12345")
    
     def test_credentials_instance(self):
            """Method that tests whether the new_credentials have been instantiated correctly"""
        self.assertEqual(self.new_credentials.account_name, "Facebook")
        self.assertEqual(self.new_credentials.account_password, "12345")