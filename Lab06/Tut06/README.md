# Tutorial 1

 - Networks & HTTP
 - Flask
 - CRUD
 - State
 - Authentication
 - Authorisation

## Activities

### Activity 1 - API
 Break into groups of 3. The only rule is that no one in the group of 3 can be in your project team. In your team, you will be given 5-10 minutes to analyse the current API specification by Sally/Bob, and to (as a team) propose one (or a couple) of new "route(s)" (i.e. url) to the interface to add some cool functionality to the product. Find something that you as a team get excited about. You'll be sharing your answer with the class, and will be expected to provide for each route:
  * A route (i.e. /this/url/name)
  * A CRUD method (e.g. GET)
  * Input parameters
  * Return object
  * Description of what it does

## Questions

### A. Networks

A.1. What is the difference between the internet and the world wide web? What network protocols are used in each?

### B. HTTP

B.1. What are the key components of an HTTP URL, such as http://unsw.com/calendar/view?term=t3&week=5#top

B.2. What is a route? What looks like it might be wrong with the design of this route?
```python
from json import dumps
from flask import Flask, request

APP = Flask(__name__)

@APP.route('/auth/login', methods=['GET'])
def auth_login():
	username = request.args.get('username')
	password = request.args.get('password')
	if password == getPassword(username):
	    return {
	        token: getToken(username) # Assume this function works
	    }
	else:
		raise ValueError("Bad password")

if __name__ == '__main__':
    APP.run()
```

B.3. What is an API? What are some examples of APIs you may have used or may use in the future?

### C. CRUD

C.1. How do we access data passed in on GET, POST, PUT, DELETE?

### D. State

D.1. Looking at the [Point server](https://gitlab.cse.unsw.edu.au/COMP1531/19T3-lectures/blob/master/week4/point/server.py) from the week 4 lectures, what challenges would we face when trying to test this with the code below?
```python
# Test that a point can be set with the right values
def test_1():
    global point
    point = Point(1, 1)
    assert(point.getX() == 1)
    assert(point.getY() == 1)

# Test that an unmodified point starts as none
def test_2():
	global point
	assert(point is None)
```


### E. Authentication

E.1. What is the difference between authentication and authorisation? Provide an example of the difference between the two.