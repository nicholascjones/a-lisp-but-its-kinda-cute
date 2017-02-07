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
				return

		self.tokenized = tokenized
		#return self.tokenized

	def parse_token(self):

		s = self.tokenized.pop(0)
		print s
		if s is '(' or s is ')':
			token = s
		elif s in self.tokens:
			token = s
		elif s.isalpha() or s.isdigit():
			token = s

		return token

	def parse_expression(self):
		left = None
		right = None
		token = self.parse_token()
		if token is ')':
			pass
		if token is '(':
			token = self.parse_token()
			left = self.parse_expression()
			if left:
				right = self.parse_expression()
			if right:
				self.parse_token()

		return ParseNode(token, left, right)


		


t1 = '(hey guys (j) sup )'


p = ParseNode()
p.read_text_format(t1)
Z = p.parse_expression()
print Z.tokenized
print Z.left
print Z.right




