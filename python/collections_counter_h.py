from collections import Counter

def main():

    n_shoes = int(input())
    shoes_stock = Counter(input().split())

    customers = int(input())

    result = 0

    for _ in range(customers):
        size_shoe, price = input().split()

        if size_shoe in shoes_stock.keys():
            if shoes_stock[size_shoe] > 0:
                shoes_stock[size_shoe] -= 1
                result += int(price)

    print(result)

if __name__ == '__main__':
    main()