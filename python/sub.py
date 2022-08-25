import re

def process_re(line):
    pattern1 = re.compile("\s&&\s")
    pattern2 = re.compile("\s\|\|\s")
    result = line
    while re.search(pattern=pattern1, string=result) != None:
        result = re.sub(pattern1," and ",result)
    while re.search(pattern=pattern2, string=result) != None:
        result = re.sub(pattern2," or ", result, count=0)
    
    return result

keyboard = [
    "x&& &&& && && x || | ||\|| x"
]

for line in keyboard:
    print(process_re(line))