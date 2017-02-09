#!/usr/bin/env python
from string import *
import sys

tokens = set(['+','-','/','*','<','>','?','(',')','eq?','max','min','define','||','&&','strcar','strcdr'])


vs = {}

class ParseNode:

	def __init__(self, tokenized=None, left=None, right=None, flt = False):
		self.flt = True
		"""
		if tokenized.isdigit():
			print tokenized
			if isinstance(tokenized, float):
				print "nice, float"
				self.flt = True
			else:
				print "nah, int"
				self.float = False
		"""
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
		#print 'right'
		evaluate_r(n.right,stack)
	if n.left:
		#print 'left'
		evaluate_r(n.left,stack)

	if n.tokenized.isdigit():
		if n.flt:
			stack.append(float(n.tokenized))
		else:
			stack.append(int(n.tokenized))
		#print stack
	elif n.tokenized.isalpha() and n.tokenized not in tokens:
		if n.tokenized in vs:
			stack.append(float(vs[n.tokenized]))
		else:
			stack.append(n.tokenized)
		#print stack
	else:
		#print 'stack'
		#print stack
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
			stack.append(val==stack.pop())
		elif n.tokenized == '<':
			stack.append(val<stack.pop())
		elif n.tokenized == '>':
			stack.append(val>stack.pop())
		elif n.tokenized == '||':
			v2 = stack.pop()
			if ((bool(val) or (bool(v2)))):
				stack.append('#t')
			else:
				stack.append('#f')
			"""
			if ((bool(val) or (bool(v2)))):
				stack.append('#t')
			else:
				stack.append('#f')
			"""
			#print "orrrrrr"
			#stack.pop()
			#print val
			#stack.append(bool(val))
		elif n.tokenized == '&&':
			#print val
			#print stack.pop()
			v2 = stack.pop()
			#print "??"
			#print val
			#print stack.pop()
			#print val
			#print v2
			#print stack
			if ((bool(val) and (bool(v2)))):
				stack.append('#t')
			else:
				stack.append('#f')
			#print stack
			"""
			print (val and v2)
			print "aaaaand"
			#stack.pop()
			print val
			stack.append(val)
			"""
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
			#print "hit it"

			vs[str(val)] = stack.pop()
			stack.append(val)
			#print 'stack'
			#print stack

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


t1 = '( + (* 1 (- 2 3)) (- 69 55))'
t2 = '(- 69 55)'
t3 = '(* 100 67)'
t4 = '(/ 5 2)'
t5 = '(define a 1)'
t6 = '(min 1 2)'
t7 = '(&& 1 0)'

"""
tk = read_text_format(t7)
print tk

z = parse_expression(tk)
print z

dfs_recursive(z)

print evaluate(z)
print vs
"""

lst = read_from_file()

for ln in lst:
	t = read_text_format(ln)
	z1 = parse_expression(t)
	print evaluate(z1)
	#print vs





