import re

text = open('/Users/arkil/Data/Work/codes/reviewing/logs/28e42b62/paper.txt').read()
start = text.find('Table 1')
end = text.find('3.2. Comparative Performance Analysis', start)
print(text[start:end])
