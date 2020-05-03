#This program is a basis of regex (Regular Expression)

import re
numRegex=re.compile(r'\d\d\d\d')
st = input('4 digit')
mo = numRegex.search(st)
print('Answer :' + mo.group())