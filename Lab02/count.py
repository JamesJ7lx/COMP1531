from collections import OrderedDict 

def count_char(input):
    # returns string with no duplicates
    noDup = "".join(OrderedDict.fromkeys(input))
    
    # count occurences 
    occurences = []
    for i in noDup:
    	occurences.append(count_occur(i, input))
    
    # create dictionary 	
    return create_dictionary(noDup, occurences)
    pass

# returns number of a character occurs in input
def count_occur(j, input):
	count = 0
	for i in input: 
		if j.find(i) != -1:
			count += 1
	return count

# prints dictionary
def create_dictionary(noDup, occurences):
	dic = {}
	for i in range(len(noDup)):
		dic[noDup[i]] = occurences[i]
	return dic
