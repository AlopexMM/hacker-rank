def main():
    t = int(input().strip())

    for _ in range(t):
        n = int(input().strip())
        f1 = 0
        f2 = 1
        result = 0
        for _ in range(2, n):
            fn = f1 + f2
            if fn > n:
                break
            else:
                f1 = f2
                f2 = fn
            if fn % 2 == 0:
                result += fn
        print(result)


if __name__ == '__main__':
    main()