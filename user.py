class User:
    '''
    generate new class instance of user
    '''
    users= []
    def __init__ (self,username,password):
        '''
        #__init__ method that defines our objects
        '''

        self.username = username
        self.password= password

    def save_user(self):
       
        User.users.append(self)


    @classmethod
    def find_user_byUsername(cls,password):
      

        for user in cls.users:
            if user.username == username:
                return user


    @classmethod
    def user_auth(cls,username,password):
        
        for user in cls.user_list:
            if user.username == username and user.password == password:
                return True


    @classmethod
    def user_registered(cls,username):

        for user in cls.user_list:
            if user.username == username:
                return True

            return False
