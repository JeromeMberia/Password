from user import User
import credentials 

import requests
from random import randint
from credentials import Account


url='https://raw.githubusercontent.com/dwyl/english-words/master/words.txt'

r = requests.get(url)
text = r.text
individual_words = text.split()
random_number = randint(0,len(individual_words))
password2 = str(individual_words[random_number] + str(random_number))


  

def create_account(a_name,u_name,pass_word):
    '''
    Function to create a new account
    '''
    new_account = Account(a_name,u_name,pass_word)
    return new_account

def save_accounts(Account):
    '''
    Function to save account
    '''
    Account.save_account()

def del_account(Account):
    '''
    Function to delete a account
    '''
    Account.delete_account()

def find_account(account_name):
    '''
    Function that finds a account by number and returns the account
    '''
    return Account.find_account(account_name)

def check_existing_accounts(account_name):
   
    return Account.find_account(account_name)


def main():
        pass_word = password2 
        print("Hello, What name would like use to call you?")
        master_name = input()
        print("Please enter your master password :")
        master_password = input()

        print(f"Hello {master_name}. what would you like to do?")
        print('\n')

        while True:
                print("Use these short codes :")
                print(" cc - create a new account")
                print(" dc - display accounts")
                print(" fc -find a account")
                print(" ex -exit the account list")
                short_code = input().lower()

                if short_code == 'cc':
                        #account
                        print("New account")
                        print("-"*10)

                        #account_name
                        print("Please type in the account:(Facebook, Twitter, Gmail e.t.c)")
                        a_name = input()

                        #user_name
                        print("Username:")
                        u_name = input()
                        #password
                        print ("Do you what us to generate a password for you ....(yes or no)")
                        shortcode = input()
                        if shortcode == 'yes':
                                password = pass_word
                                print(f"your password is {password} ")
                        else:
                                print("enter your password")
                                password = input()
                        #Saves the credentials
                        save_accounts(create_account(a_name,u_name,password))

                        print ('\n')
                        print(f"you have succesfully created your new credentials for {a_name} account")
                        print ('\n')


                        
                        

                elif short_code == 'dc':

                        if Account.display_account():
                                print("Here is a list of all your accounts")
                                print('\n')

                                for account in Account.display_account():
                                        print("Account          Username          Password")
                                        print(f"{account.account_name}            {account.username}         {account.password}")

                                print('\n')
                        else:
                                print('\n')
                                print("You dont seem to have any accounts saved yet")
                                print('\n')

                elif short_code == 'fc':

                        print("Enter the account you want to search for")

                        search_account = input()
                        if check_existing_accounts(search_account):
                                search_account = find_account(search_account)
                                print(f"{Account.search_account.account_name}")
                                print('-' * 20)

                                print(f"Username: .......{search_account.user_name}")
                                print(f"Password: .......{search_account.password}")
                        else:
                                print("That account does not exist")

                elif short_code == "ex":
                        print("Bye .......")
                        break
                else:
                        print("Invalid Input! ")

if __name__ == '__main__':
    main()