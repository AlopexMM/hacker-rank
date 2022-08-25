import re

n = "qwrtypsdfghjklzxcvbnm"
m = "aeiou"
group_words = re.findall(r'(?<=[%s])([%s]{2,})[%s]' % (n,m,n), input(),flags=re.I)
print('\n'.join(group_words or ['-1']))