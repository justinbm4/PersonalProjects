from Id import Id
import Expr
from Core import Core
import sys

class Factor:

	def parse(self, parser):
		if parser.scanner.currentToken() == Core.ID:
			self.id = Id()
			self.id.parse(parser)
		elif parser.scanner.currentToken() == Core.CONST:
			self.constant = parser.scanner.getCONST()
			parser.scanner.nextToken()
		elif parser.scanner.currentToken() == Core.LPAREN:
			parser.scanner.nextToken()
			self.expr = Expr.Expr()
			self.expr.parse(parser)
			parser.expectedToken(Core.RPAREN)
			parser.scanner.nextToken()
		else:
			print("ERROR: Expected ID, CONST, or LPAREN, recieved " + parser.scanner.currentToken().name + "\n", end='')
			sys.exit()
	
	def semantic(self, parser):
		if hasattr(self, 'id'):
			self.id.semantic(parser)
		elif hasattr(self, 'expr'):
			self.expr.semantic(parser)
	
	def print(self):
		if hasattr(self, 'id'):
			self.id.print()
		elif hasattr(self, 'expr'):
			print("(", end='')
			self.expr.print()
			print(")", end='')
		else:
			print(self.constant, end='')

	def execute(self, memory):
		num1=0
		if hasattr(self, 'id'):
			num1 = memory.getIdVal(self.id.identifier)
		elif hasattr(self, 'expr'):
			num1 = self.expr.execute(memory)
		else:
			num1 = self.constant
		return num1