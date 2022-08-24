import re

s = input()
k = input()

pattern = re.compile(f'{k}')
r = pattern.search(s)
if r == None:
    print('(-1, -1)')
else:
    while r:
        print(f'({r.start()}, {r.end() - 1})')
        r = pattern.search(s,r.start()+1)