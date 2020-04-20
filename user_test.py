import unittest
from user import User
from credentials import Account
class TestUser(unittest.TestCase):
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("James","james123") 


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.username,"James")
        self.assertEqual(self.new_user.password,"james123")
    
     
          
if __name__=='__main__':
    unittest.main()