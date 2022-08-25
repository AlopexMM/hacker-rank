"""
Inputs are 
2
9587456281
1252478965

3
8956324712
FACBGEGADB
85234789651

Valid numbers start with 9,8 or 7
And has to be a ten digit number
"""
import re

n = int(input())

for _ in range(n):
    match = re.match(r"^[987][0-9]{9}$",input())
    if match != None:
        print("YES")
    else:
        print("NO")