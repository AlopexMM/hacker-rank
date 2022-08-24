def fun(s):
    # return True if s is a valid email, else return False
    import re
    regex = re.compile(r'[\w-]+@[a-zA-Z0-9]+\.[A-Z|a-z]+')
    if s.find('@') == -1:
        return False
    if re.fullmatch(regex,s) != None:
        s_extension = s.rsplit('.',1)[1]
        if len(s_extension) > 3:
            return False
        return True
    else:
        return False
    

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    emails = [
        'its@gmail.com1',
        'mike13445@yahoomail9.server',
        'rase23@ha_ch.com',
        'daniyal@gmail.coma',
        'thatisit@thatisit',
    ]

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)