from collections import Counter

def main():
    n = int(input()) # Number of words inputs
    words = Counter()

    for _ in range(n):
        word = input()
        words[word] += 1    
    
    count_words = ''

    for value in words.values():
        count_words += f'{str(value)} '
    
    print(f'{len(words.keys())}\n{count_words}')
    

if __name__ == '__main__':
    main()