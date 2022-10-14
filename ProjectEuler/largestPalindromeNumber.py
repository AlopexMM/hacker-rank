"""
Find the largest palindrome made from the product of three digits numbers which is less than N

Test input
2
101110
800000

Test output
101101
793397
"""


def is_palindrome(number: int) -> bool:
    str_number = str(number)
    reverse_number = str_number[::-1]
    return True if str_number == reverse_number else False


def main():
    t = int(input().strip())

    for _ in range(t):
        n = int(input().strip())
        r_palindrome = 0
        num = n - 1
        flag = False
        while num > 100001:
            if is_palindrome(num):
                for i in range(1000, 99, -1):
                    num_divided = str(num / i).split(".")
                    if num_divided[1] == "0" and len(num_divided[0]) == 3:
                        r_palindrome = num
                        flag = True
                        break
            if flag:
                break
            num -= 1
        print(r_palindrome)


if __name__ == "__main__":
    main()
