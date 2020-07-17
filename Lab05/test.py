



database = {"channels": [{"Private": 0, "Channel_ID": "001", "Members": [444], "Name": "SUP"}, {"Private": 1, "Channel_ID": "002", "Members": [44], "Name": "HEY"}], "users": [{"u_id": 1, "email": "marcr@gmail.com", "password": "c6327a7a5ff8711d5042168913309a1ab0e282de7939724816ad35ce31a35a5f", "name_first": "Marc", "name_last": "John"}], "messages": [{"001": {"Sent_by": "userID", "Reacts_by": "", "Content": "", "Pinned": "Appl", "in_Channel": "channelID"}}]}
channel_id = "001"
add_channel = 0
for add_channel in database['channels']:
	# If token is a valid token set 'valid' to 1
	if channel_id == add_channel['Channel_ID']:
		print("HI")
		break

channel = database["channels"]['Channel_ID']
channel['Members'].append(666)
channel['Members'].append(666)

print(database["channels"])





















	

# for foo in xrange(10):
#     bar = 2
# print(foo, bar)

# from flask import Flask, redirect, url_for, request
# app = Flask(__name__)

# @app.route('/success/<name>')
# def success(name):
#    return 'welcome %s' % name

# @app.route('/login',methods = ['POST', 'GET'])
# def login():
#    if request.method == 'POST':
#       user = request.form['nm']
#       return redirect(url_for('success',name = user))
#    else:
#       user = request.args.get('nm')
#       return redirect(url_for('success',name = user))

# if __name__ == '__main__':
#    app.run(debug = True)



# from flask import Flask, send_file
# APP = Flask(__name__)

# # HELLO WORLD
# @APP.route("/")
# def hello():
#     return "Hello World!"
 
# # IMAGE 
# @APP.route("/img")
# def img():
#     return send_file('./cat.jpg', mimetype='image/jpg')
 
# if __name__ == "__main__":
#     APP.run()

# from flask import Flask, jsonify

# app = Flask(__name__)


# # tasks = [
# #     {
# #         'id': 1,
# #         'title': u'Buy groceries',
# #         'description': u'Milk, Cheese, Pizza, Fruit, Tylenol', 
# #         'done': False
# #     },cur
# #     {
# #         'id': 2,
# #         'title': u'Learn Python',
# #         'description': u'Need to find a good Python tutorial on the web', 
# #         'done': False
# #     }
# # ]

# # @app.route('/todo/api/v1.0/tasks', methods=['GET'])
# # def get_tasks():
# #     return jsonify({'tasks': tasks})

# # if __name__ == '__main__':
#     app.run(debug=True)