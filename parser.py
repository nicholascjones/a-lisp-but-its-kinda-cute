from string import *

tokens = set(['+','-','/','*','<','>','?','(',')'])

class ParseNode:

	def __init__(self, tokenized=None, left=None, right=None):
		self.tokenized = None
		self.left = left
		self.right = right
		#self.tokens = set(['+','-','/','*','<','>','?','(',')'])



def read_text_format(txt):
	tokenized = []
	txt = txt.replace('(',' ( ')
	txt = txt.replace(')',' ) ')
	for term in txt.split():
		if term in tokens or term.isalpha() or term.isdigit(): #checks for validity
			tokenized.append(term)
		else:
			print "Syntax error"
			return

	return tokenized

def parse_token(tokenized):

	s = tokenized.pop(0)
	#print s
	if s is '(' or s is ')':
		token = s
	elif s in tokens:
		token = s
	elif s.isalpha() or s.isdigit():
		token = s

	return token

def parse_expression(tokenized):
	left = None
	right = None
	token = parse_token(tokenized)
	#print "token = " + str(token)
	if token == ')':
		pass
	if token == '(':
		#print "took branch"
		token = parse_token(tokenized)
		#print "new token = " + str(token)
		#print "left should be: " + str(parse_expression(tokenized))
		left = parse_expression(tokenized)
		#print "left = " + str(left)
		if left:
			right = parse_expression(tokenized)
		if right:
			parse_token(tokenized)
	return ParseNode(token, left, right)


def dfs_recursive(rt):
	print parse_expression()

t1 = '( + 1 (- 2 3))'


tk = read_text_format(t1)
#print tk
z = parse_expression(tk)
print z.left
print z.right
#print z.left.tokenized
#print z.right.tokenized


"""
print Z.tokenized
print Z.left
print Z.right
"""



