from string import *

tokens = set(['+','-','/','*','<','>','?','(',')','eq?','max','min','abs'])

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


		#self.tokens = set(['+','-','/','*','<','>','?','(',')'])



def read_text_format(txt):
	tokenized = []
	txt = txt.replace('(',' ( ')
	txt = txt.replace(')',' ) ')
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
	elif s.isalpha or s.isnum():
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
		evaluate_r(n.right,stack)
	if n.left:
		evaluate_r(n.left,stack)
	if n.tokenized.isdigit():
		if n.flt:
			stack.append(float(n.tokenized))
		else:
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
		elif n.tokenized == "eq?":
			stack.append(val==stack.pop())
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


def evaluate(n):

	s = []
	evaluate_r(n,s)

	try: 
		return s[-1]
	except:
		return None


t1 = '( + (* 1 (- 2 3)) (- 69 55))'
t2 = '(- 69 55)'
t3 = '(* 100 67)'
t4 = '(/ 5 2)'
t5 = '(def a 1)'
t6 = '(min 1 2)'



tk = read_text_format(t6)

z = parse_expression(tk)

dfs_recursive(z)

print evaluate(z)






