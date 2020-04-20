class Account:

  accounts = []
  def __init__(self,account_name,username,password):
    
    self.account_name = account_name
    self.username = username
    self.password = password
  
  def save_account(self):

    Account.accounts.append(self)
  
  def delete_account(self):

    Account.accounts.remove(self)
  
  def display_account(self):
    
    return Account.accounts
  
  def find_account(self):
    
    return Account.find_account(account_name)

  @classmethod
  def display_account(self):  
    return self.accounts
  
  