def minion_game(string):    
    # your code goes here
    # Vowels Kevin and Stuart consonants
    vowels = "AEIOU"
    kevin_words = 0
    stuart_words = 0
    for i in range(len(string)):
        if string[i] in vowels:
            kevin_words += len(string) - i
        else: 
            stuart_words += len(string) - i
    # output an print of the name and the count of words
    if kevin_words > stuart_words:
        print("Kevin {0}".format(kevin_words))
    elif kevin_words < stuart_words:
        print("Stuart {0}".format(stuart_words))
    else:
        print("Draw")

if __name__ == "__main__":
    minion_game("BANANA")