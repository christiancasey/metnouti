import sys
import os
import re

def printHeading():
	print('\n'*100)
	print('𓉗'*81)
	print('𓉗\t\t\t\t\t𓉐  𓋹𓉐\t\t\t\t\t𓉗')
	print('𓉗\t\t\t\tAn interpreter for 𓊹𓌃\t\t\t\t𓉗')
	print('𓉗'*81)
	print('\n'*2)


sCode = '𓂜𓈖𓃹𓈖𓏞𓊹𓌃'
if len(sys.argv) > 1:
	
	printHeading()
	
	sFilename = sys.argv[1]
	
	# Make sure the file ends in .𓊹𓌃
	_, sExt = os.path.splitext(sFilename)
	if not sExt == '.𓊹𓌃':
		raise Exception('Invalid 𓊹𓌃 file: %s' % sFilename)
	
	with open(sFilename,'r') as f:
		sCode = f.read()
		f.close()
	
	iStart = sCode.find('𓆓𓌃')
	if iStart >= 0:
		
		sCode = sCode[iStart:]
		print(sCode)
		print('\n'*3)
		
		# Make sure that everything in the program is in hieroglyphs
		# Except string literals (preceded by 𓀁)
		sCodeNoString = sCode
		sCodeNoString = re.sub('𓀁([^\n]*)\n', '', sCodeNoString)
		sCodeNoString = re.sub('[𓀀-𓐮\s]*', '', sCodeNoString)
		
		print(sCodeNoString)
		print(len(sCodeNoString))
		
else:
	print(sCode)
	
	
print('\n'*3)