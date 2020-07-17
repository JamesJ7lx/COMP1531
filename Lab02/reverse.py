

def reverseWords(string_list):
	output = []
	for i in string_list:
	    words = i.split(" ") 
	    # slicing to reverse the list
	    words = words[-1::-1] 
	    reverse_string = ' '.join(words)
	    output.append(reverse_string)
	return output
	pass

def test_reverse_words_short():

	string_list = ["Hello World", "I am here"]
	assert reverseWords(string_list) == ["World Hello", "here am I"]

	string_list = ["My name", "is", "Marc Rocca"]
	assert reverseWords(string_list) == ["name My", "is", "Rocca Marc"]

	string_list = ["Yoda the", "force strong", "it is"]
	assert reverseWords(string_list) == ["the Yoda", "strong force", "is it"]

	string_list = ["apples are", "nice", "this season"]
	assert reverseWords(string_list) == ["are apples", "nice", "season this"]

def test_reverse_words_long():

	string_list = ["m a", "a d", "d a", "a m", "m i", "i m", "m a", "a d", "d a", "a m", "m"]
	assert reverseWords(string_list) == ["a m", "d a", "a d", "m a", "i m", "m i", "a m", "d a", "a d", "m a", "m"]

def test_reverse_words_random():

	string_list = ["asdfgh sdfghj dfghjk"]
	assert reverseWords(string_list) == ["dfghjk sdfghj asdfgh"]

def test_reverse_words_noChange():

	string_list = ["Here's", "Johnny"]
	assert reverseWords(string_list) == ["Here's", "Johnny"]

	string_list = [""]
	assert reverseWords(string_list) == [""]

	string_list = ["Blue", "Kites", "Fly", "High"]
	assert reverseWords(string_list) == ["Blue", "Kites", "Fly", "High"]
