# abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1357902468
inp = '1qaz2wsx3edc4rfv5tgb6yhn7ujm8ik9ol0pQWERTYUIOPASDFGHJKLZXCVBNM'


de = ''
do = ''
sl = ''
su = ''
for c in inp:
    if c.isalpha():
        if c.islower():
            sl += c
        elif c.isupper():
            su += c
    if c.isdigit():
        d = int(c)
        if d % 2 == 0:
            de += c
        else:
            do += c

sl = str(sorted(sl)).strip('[').strip(']').replace('\'','').replace(',','').replace(' ','')
su = str(sorted(su)).strip('[').strip(']').replace('\'','').replace(',','').replace(' ','')
do = str(sorted(do)).strip('[').strip(']').replace('\'','').replace(',','').replace(' ','')
de = str(sorted(de)).strip('[').strip(']').replace('\'','').replace(',','').replace(' ','')
print('{0}{1}{2}{3}'.format(sl,su,do,de))