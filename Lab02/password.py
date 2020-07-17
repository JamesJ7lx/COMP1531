
def check_password(password):
    '''
    Takes in a password, and returns a string based on the strength of that password.

    The returned value should be:
    * "Strong password", if at least 12 characters, contains at least one number, at least one uppercase letter, at least one lowercase letter.
    * "Moderate password", if at least 8 characters, contains at least one number.
    * "Poor password", for anything else
    * "Horrible password", if the user enters "password", "iloveyou", or "123456"
    '''
    horrible = ["password", "iloveyou", "123456"]
    for i in horrible:
        if password == i:
            return "Horrible password"

    if any(i.isdigit() for i in password):
        if len(password) >= 12:
            if not (password.isupper()) and not (password.islower()):
                return "Strong password"
            else:
                return "Moderate password"
        elif len(password) >= 8:
            return "Moderate password"
        else: 
            return "Poor password"
    else:
        return "Poor password"
    pass

'''
if __name__ == '__main__':
    print(check_password("ihearttrimesters"))
'''
def test_horrible():
    password = 'password'
    assert check_password(password) == 'Horrible password'
    password = 'iloveyou'
    assert check_password(password) == 'Horrible password'  
    password = '123456'
    assert check_password(password) == 'Horrible password'

def test_poor():
    password = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    assert check_password(password) == 'Poor password'
    password = 'Hello12'
    assert check_password(password) == 'Poor password'  
    password = ' '
    assert check_password(password) == 'Poor password'    

def test_moderate():
    password = '1ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    assert check_password(password) == 'Moderate password'
    password = 'Hello123'
    assert check_password(password) == 'Moderate password'  
    password = '1abcdefghijklmnopqrstuvwxyz'
    assert check_password(password) == 'Moderate password'    

def test_strong():
    password = '1abcDEFGHIJKLMNOPQRSTUVWXYZ'
    assert check_password(password) == 'Strong password'
    password = 'Hello1234567'
    assert check_password(password) == 'Strong password'  
    password = '1ABCdefghijklmnopqrstuvwxyz'
    assert check_password(password) == 'Strong password'    
