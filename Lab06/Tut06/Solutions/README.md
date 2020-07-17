### A.1.

Internet is a network where computers communicate over a series of protocols, SSH, FTP, HTTP, IMAP, SMTP.

The world wide web is a network where people use URLs sent over HTTP to access documents and resources

### B.1. 
 * **Protocol: http**
   * This is the network protocol used
 * **Domain: unsw.com**
   * This is the key used on DNS servers to look up a particular IP. Think of DNS servers like a dictionary of domain:IP pairs
 * **Path: calendar/view**
   * This denotes the specific page/resource you want to view
 * **Query string: ?term=t3&week=5**
   * Another way of passing data to the server via the URL. Nowadays this is often more integrated into the path
 * **Anchor: top**
   * Information often used to deermine the particular state of the same resource loaded from the server. Common uses for this will be the anchor will specify a particular COMMENT on a forum to "jump" to after loading a forum page

### B.2. 
* A route is a path for your flask server
* Issues:
  * Raising a value error like that will just cause the server to raise an exception, you would actually need to return something more meaningful

### B.3.
* An API (application program interface) is a set of functions and capabilities that describe a system or service

### C.1.

For all:

```python
from flask import request
```

For GET:
```python
request.args.get('argument_key')
```

For POST, PUT, DELETE
```python
request.form.get('argument_key')
```

Try to link up CRUD to GET/POST/PUT/DELETE, as per lectures

### D.1.

The main challenge is that the state of the program won't be reset between functions. One simple way to solve this is to write a global function called "reset" which when called resets the state of the data.

```python

def dataReset():
    global point
    point = None

def dataGet():
    global point
    return point

def test_2():
    dataReset()
    data = dataGet()
    assert(data is None)
    
```

### E.1.

Authentication: Confirming an identity
Authorisation: Providing access to resources based on their identity

E.G. auth/login is a function that authenticates a user, then on subequent function clals a token is passed in to authorise access to that particular route.
