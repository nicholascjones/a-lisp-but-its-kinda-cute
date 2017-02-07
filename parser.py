from string import *


class ParseNode:

	def __init__(self, txt, left=None, right=None, tokens=None):
		self.txt = txt
		self.left = left
		self.right = right
		self.tokens = set(['+','-','/','*','<','>','?','(',')'])



	def read_text_format(self):
		tokenized = []
		self.txt = self.txt.replace('(',' ( ')
		self.txt = self.txt.replace(')',' ) ')
		for term in self.txt.split():
			if term in self.tokens or term.isalpha() or term.isdigit(): #checks for validity
				tokenized.append(term)

		return tokenized


t1 = '(hey guys (j) sup )'


p = ParseNode(t1)

print p.read_text_format()