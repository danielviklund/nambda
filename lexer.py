"""
To lex or not to lex - that is the question.

Will break up the nambda source code into TOKENS and VALUES.
"""

def lex(filepath):
	# Open file.
	file = open(filepath, 'r');
	# Save contents of file
	# Tokenize contents
