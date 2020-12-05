from collections import Counter

def main():
    s = list(input())

    s.sort()

    most_common = Counter(s).most_common(3)

    result = ''

    for x in most_common:
        result += '{} {}\n'.format(x[0],x[1])

    print(result)
    


if __name__ == '__main__':
    main()