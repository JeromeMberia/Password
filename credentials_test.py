import unittest
from user import User
from credentials import Account

class TestAccount(unittest.TestCase):
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_account = Account("Gmail","James","james123") 
    
    def tearDown(self):
        '''
        The tear down method which will clean up after every test case is complete
        '''

        Account.accounts = []

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_account.account_name,"Gmail")
        self.assertEqual(self.new_account.username,"James")
        self.assertEqual(self.new_account.password,"james123")
    
    def test_save_account(self):
        
        self.new_account.save_account()
        self.assertEqual(len(Account.accounts),1)  
    
    def test_display_all_account(self):
        '''
        method that returns a list of all contacts saved
        '''

        self.assertEqual(Account.display_account(),Account.accounts)
          
if __name__=='__main__':
    unittest.main()