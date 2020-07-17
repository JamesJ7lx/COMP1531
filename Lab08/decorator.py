import sys

MESSAGE_LIST = []

def authorised(auth_token):
    def wrapper(*args, **kwargs):
        if list(args)[0] == "CrocodileLikesStrawberries":
            return function(*args, **kwargs)
        else:
            raise ValueError("Invalid authentication")
    return wrapper

@authorised
def get_messages(auth_token):
    return MESSAGE_LIST
@authorised
def add_messages(auth_token, msg):
    global MESSAGE_LIST
    MESSAGE_LIST.append(msg)

if __name__ == '__main__':
    auth_token = ""
    if len(sys.argv) == 2:
        auth_token = sys.argv[1]

    add_messages(auth_token, "Hello")
    add_messages(auth_token, "How")
    add_messages(auth_token, "Are")
    add_messages(auth_token, "You?")
    print(get_messages(auth_token))
