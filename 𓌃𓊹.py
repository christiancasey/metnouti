import sys
import os
import re

def colored(sCode, sString):
	return '\x1b[%sm%s\x1b[0;37;40m' % (sCode, sString)

def printError(s):
	print(colored('5;33;41', s))

def printGlyphs(s):
	s = re.sub(r'([𓀀-𓐮])', r'\1 ', s)
	return s.strip()

def print_format_table():
	"""
	prints table of formatted text format options
	"""
	for style in range(8):
		for fg in range(30,38):
			s1 = ''
			for bg in range(40,48):
				format = ';'.join([str(style), str(fg), str(bg)])
				s1 += '\x1b[%sm %s \x1b[0m' % (format, format)
			print(s1)
		print('\n')



def printHeading():
	print('\n'*100)
	print('𓉗'*81)
	print('𓉗\t\t\t\t\t𓉐  𓋹𓉐\t\t\t\t\t𓉗')
	print('𓉗\t\t\t\tAn interpreter for 𓊹𓌃\t\t\t\t𓉗')
	print('𓉗'*81)
	print('\n'*2)

def interpret(sFilename):
	
	# Make sure the file ends in .𓊹𓌃
	_, sExt = os.path.splitext(sFilename)
	if not sExt == '.𓊹𓌃':
		raise Exception('\nInvalid 𓊹𓌃 file: %s' % sFilename)
	
	with open(sFilename,'r') as f:
		sCode = f.read()
		f.close()
	
	# Make sure there are leading and trailing newlines so regex works
	sCode = '\n%s\n' % sCode
	
	# Print out the original code (for debugging)
	print(colored('0;30;46', printGlyphs(sCode)))
	
	# Find the program start marker: 𓆓𓌃
	iStart = sCode.find('\n𓆓𓌃')
	if iStart >= 0:
		
		sCode = sCode[iStart+3:]
		if len(sCode) < 2:
			printError(printGlyphs('𓂜𓈖𓃹𓈖𓏞𓊹𓌃'))
			return
		
		# If the program has a title
		sTitle = ''
		if sCode[:2] == '𓇋𓈖':
			iTitleEnd = sCode.find('\n')
			sTitle = sCode[2:iTitleEnd]
		
		print(colored('0;30;47', printGlyphs('𓂋𓈖𓍷 ' + sTitle)))
		print('\n'*3)
		
		# Make sure that everything in the program is in hieroglyphs
		# Except string literals (preceded by 𓀁)
		sCodeNoString = sCode
		sCodeNoString = re.sub('𓀁([^\n]*)\n', '', sCodeNoString)
		sCodeNoString = re.sub('[𓀀-𓐮\s]*', '', sCodeNoString)
		if len(sCodeNoString):
			print(colored('5;33;41', '\nInvalid 𓊹𓌃 file: %s\nNon-glyph characters found.' % sFilename))
		
		print(sCodeNoString)
		print(len(sCodeNoString))


if len(sys.argv) > 1:
	
	printHeading()
	
	print_format_table()
	
	sFilename = sys.argv[1]
	
	interpret(sFilename)
		
else:
	print(colored('5;33;41', '𓂜𓈖𓃹𓈖𓏞𓊹𓌃'))
	
	
print('\n'*3)