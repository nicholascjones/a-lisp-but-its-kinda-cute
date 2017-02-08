from string import *

tokens = set(['+','-','/','*','<','>','?','(',')'])

class ParseNode:

	def __init__(self, tokenized=None, left=None, right=None):
		self.tokenized = tokenized
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

	#print "token = " + str(token)
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
	print "(Node: value = " + str(rt.tokenized)
	if rt.left:
		dfs_recursive(rt.left)
		print "left = " + str(rt.left.tokenized)
	if rt.right:
		dfs_recursive(rt.right)
		print "right = " + str(rt.right.tokenized)
	print ")"

## use list as stack! append pop
def evaluate_r(n, stack):

	val=0
	if n.right:
		evaluate_r(n.right,stack)
	if n.left:
		evaluate_r(n.left,stack)
	if n.tokenized.isdigit():
		stack.append(int(n.tokenized))
	else:
		val = stack.pop()
		if n.tokenized == "+":
			val += stack.pop()
			stack.append(val)
		elif n.tokenized == "-":
			val -= stack.pop()
			stack.append(val)
		elif n.tokenized == "/":
			val /= stack.pop()
			stack.append(val)
		elif n.tokenized == "*":
			val *= stack.pop()
			stack.append(val)


def evaluate(n):

	s = []
	evaluate_r(n,s)

	return s[-1]


t1 = '( + 1 (- 2 3))'
t2 = '(- 69 55)'


tk = read_text_format(t2)

z = parse_expression(tk)

dfs_recursive(z)

print evaluate(z)





