#!/usr/bin/env python
from string import *
import sys

tokens = set(['+','-','/','*','<','>','?','(',')','eq?','max','min','define','||','&&'])

vs = {}

class ParseNode:

	def __init__(self, tokenized=None, left=None, right=None, flt = False):
		self.flt = True
		self.tokenized = tokenized
		self.left = left
		self.right = right

def read_text_format(txt):
	tokenized = []
	txt = txt.replace('(',' ( ')
	txt = txt.replace(')',' ) ')
	#txt = txt.replace('#t','1')
	#txt = txt.replace('#f','0')
	for term in txt.split():
		if term in tokens:
			tokenized.append(term)
		elif term.isalnum():
			tokenized.append(term)

	return tokenized

def parse_token(tokenized):
	s = tokenized.pop(0)
	token = ''
	#print s
	if s is '(' or s is ')':
		token = s
	elif s == 'define':
		token = s
	elif s in tokens:
		token = s
	elif s.isalpha() or s.isdigit():
		token = s

	#print "token = " + str(token)
	#print token
	return token

def parse_expression(tokenized):
	left = None
	right = None
	token = parse_token(tokenized)
	#print "token = " + str(token)
	if token == ')':
		pass
	if token == '(':
		token = parse_token(tokenized)
		left = parse_expression(tokenized)
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
		if n.flt:
			stack.append(float(n.tokenized))
		else:
			stack.append(int(n.tokenized))
	elif n.tokenized.isalpha() and n.tokenized not in tokens:
		if n.tokenized in vs:
			stack.append(float(vs[n.tokenized]))
		else:
			stack.append(n.tokenized)
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
		elif n.tokenized == "eq?":
			v2 = stack.pop()
			if val == v2:
				stack.append('#t')
			else:
				stack.append('#f')
		elif n.tokenized == '<':
			v2 = stack.pop()
			if val < v2:
				stack.append('#t')
			else:
				stack.append('#f')
		elif n.tokenized == '>':
			v2 = stack.pop()
			if val > v2:
				stack.append('#t')
			else:
				stack.append('#f')
		elif n.tokenized == '||':
			v2 = stack.pop()
			if ((bool(val) or (bool(v2)))):
				stack.append('#t')
			else:
				stack.append('#f')
		elif n.tokenized == '&&':
			v2 = stack.pop()
			if ((bool(val) and (bool(v2)))):
				stack.append('#t')
			else:
				stack.append('#f')
		elif n.tokenized == "max":
			v2 = stack.pop()
			if val >= v2:
				stack.append(val)
			else:
				stack.append(v2)
		elif n.tokenized == "min":
			v2 = stack.pop()
			if not val >= v2:
				stack.append(val)
			else:
				stack.append(v2)
		elif n.tokenized == 'strcar':
			stack.append(list(val)[0])
		elif n.tokenized == "define":
			vs[str(val)] = stack.pop()
			stack.append(val)

def evaluate(n):

	s = []
	evaluate_r(n,s)

	try: 
		return s[-1]
	except:
		return None

def to_boolean(x):
	if x == '#t':
		return True
	if x == '#f':
		return False


def read_from_file():
  
  fileInput = open(sys.argv[1], "r") # opens the file assuming it is the first argument
  
  x = fileInput.readlines() # reads the file into a list

  for i in range(0,len(x)):
    formatted = x[i].rstrip() # removes the new lines
    x[i] = formatted

  #print x # prints for checking
  return x

#lst = read_from_file()
"""
for ln in lst:
	t = read_text_format(ln)
	z1 = parse_expression(t)
	print evaluate(z1)
	#print vs
"""
"""
inp = ''
for line in sys.stdin.readlines():
	t = read_text_format(line)
	z1 = parse_expression(t)
	print evaluate(z1)
"""
inp = ''
print 'welcome to the cutest darn LISP you\'ve ever heard!'
while inp != 'quit':
	inp = raw_input(':) >>> ')
	t = read_text_format(inp)
	z1 = parse_expression(t)
	print evaluate(z1)





