

from flask import Flask, request
from json import dumps
app = Flask(__name__)
names = { [] }

@app.route('/names', methods=['GET'])
def namesshow():
    global names
    return dumps({"names" : names})

@app.route('/name/remove', methods=['DELETE'])
def remove():
    global names
    name = request.args.get('name')
    names.remove(name)
    return dumps({})

@app.route('/name/add', methods=['POST'])
def query_example():
    global names
    name = request.form.get('name') #if key doesn't exist, returns None
    names.append(name)
    print(name);
    return dumps({})

app.run()
