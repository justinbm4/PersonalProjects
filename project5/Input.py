from Id import Id
from Core import Core

class Input:
	
	def parse(self, parser):
		parser.scanner.nextToken()
		self.id = Id()
		self.id.parse(parser)
		parser.expectedToken(Core.SEMICOLON)
		parser.scanner.nextToken()
	
	def semantic(self, parser):
		self.id.semantic(parser)
	
	def print(self, indent):
		for x in range(indent):
			print("\t", end='')
		print("input ", end='')
		self.id.print()
		print(";\n", end='')

	def execute(self, memory):
		memory.inputToId(self.id.identifier)