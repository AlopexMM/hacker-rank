import re

def sortRoman(names):
    roman_letters = {"I":1, "V":5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000 }
    result = []
    names_dict = {}
    for name in sorted(names):
        n, roman = name.split(" ")
        if n not in names_dict.keys():
            names_dict[n] = {}
        k = 0
        size_roman = len(roman)
        for r in range(size_roman):
            rc = roman[r]
            r2 = r + 1
            if rc in roman_letters.keys():
                if rc == "I" and r2 != len(roman) and roman[r2] != "I":
                    k -= roman_letters[rc]
                else:
                    k += roman_letters[rc]
        if k in names_dict[n].keys():
            names_dict[n][k].append(name)
        else:
            names_dict[n][k] = [name]

    for nkeys in sorted(names_dict.keys()):
        for rkeys in sorted(names_dict[nkeys].keys(),reverse=False):
            result.append(names_dict[nkeys][rkeys])
    
    return result

if __name__ == "__main__":
    names = ['Louis IX', 'Louis VIII']

    for name in sortRoman(names):
        print(name[0])