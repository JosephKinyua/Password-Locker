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