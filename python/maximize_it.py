from itertools import product

def main():
    k, m = map(int,input().split()) # They are strings

    n = (list(map(int, input().split()[1:])) for _ in range(k)) # List of the list inputs numbers

    results = map(lambda x: sum(pow(i,2) for i in x)%m, product(*n))            

    print(max(results))

if __name__ == '__main__':
    main()