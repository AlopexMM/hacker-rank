import re
text = "__commit__"

# ([0-9])\d+|([a-z][A-Z])[a-z][A-Z]+
s = re.search(r'(([0-9])|[a-zA-Z])\1+', text)

if s != None:
    print(s.group())
else:
    print("-1")