import re
regex_pattern = re.compile("^M{,3}(C(D|M)|D?C{,3})(X(L|C)|L?X{,3})(I(X|V)|(X|V)?I{,3})$")
string = "MMMCMXCIX"
result = regex_pattern.match(string)
print(result)
#print(str(bool(re.match(regex_pattern,string))))