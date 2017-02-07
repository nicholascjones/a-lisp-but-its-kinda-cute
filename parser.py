from string import *

t1 = '(hey guys (j) sup )'


t = ['+','-','/','*','<','>','?','(',')']
tokens = set(t)

def read_text_format(txt):
	parseTree = []
	txt = txt.replace('(',' ( ')
	txt = txt.replace(')',' ) ')
	for term in txt.split():
		if term in tokens or term.isalpha() or term.isdigit(): #checks for validity
			parseTree.append(term)

	return parseTree



print read_text(t1)