import unittest
from user import User

class TestUser(unittest.TestCase):
    """
    
    Test class that defines test cases for the contact class behaviours.
    
    """
    
    def setUp(self):
        """
        
        Set Up Method to run before each test case to check if the class has been instantiated correctly
        
        """
        self.new_user = User("NewUser", "12345")
        
    def test_init(self):
        
        """
        Test to ensure that the object is initialized properly
        """
        self.assertEqual(self.new_user.user_name, "NewUser")
        self.assertEqual(self.new_user.password, "12345")