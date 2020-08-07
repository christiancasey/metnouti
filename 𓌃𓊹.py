import sys

sCode = '𓂜𓈖𓃹𓈖𓏞𓊹𓌃'
if len(sys.argv) > 1:
	with open(sys.argv[1],'r') as f:
		sCode = f.read()
		f.close()
	print(sCode)
		
else:
	print(sCode)