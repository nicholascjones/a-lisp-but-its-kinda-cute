from string import *


class ParseNode:

	def __init__(self, tokenized=None, left=None, right=None, tokens=None):
		self.tokenized = None
		self.left = left
		self.right = right
		self.tokens = set(['+','-','/','*','<','>','?','(',')'])



	def read_text_format(self,txt):
		tokenized = []
		txt = txt.replace('(',' ( ')
		txt = txt.replace(')',' ) ')
		for term in txt.split():
			if term in self.tokens or term.isalpha() or term.isdigit(): #checks for validity
				tokenized.append(term)
			else:
				print "Syntax error"
				break

		self.tokenized = tokenized


	def parse_token(self.tokenized):

		s = self.tokenized.pop(0)

		if s is '(' or s is ')':
			token = s
		elif s is in self.tokens:
			token = s
		elif s.isalpha() or s.isdigit():
			token = s

		return token

	def parse_expression(self.tokenized):
		left = None
		right = None
		token = parse_token(self.tokenized)
		if token is ')':
			print "Syntax error: cannot start with ')'"
			break
		if token is '(':
			token = parse_token(self.tokenized)
			left = parse_expression(self.tokenized)
			if left:
				right = parse_expression(s)
			if right:
				parse_token(s)

		return ParseNode(token, left, right)


		


t1 = '(hey guys (j) sup )'


p = ParseNode(t1)

print p.read_text_format()