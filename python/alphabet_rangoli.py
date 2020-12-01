import string

def print_rangoli(size):
    # your code goes here
    # per line you need a even number of dash in each side, number we recibe * 2 - 2
    
    width = (4 * size) - 3
    alphabet = string.ascii_lowercase
    for i in range(size-1,-size,-1):
        temp = '-'.join(alphabet[size-1:abs(i):-1]+alphabet[abs(i):size])
        print(temp.center(width, '-'))


if __name__ == '__main__':
    n = 5
    print_rangoli(n)
    
    # --------e--------
    # ------e-d-e------
    # ----e-d-c-d-e----
    # --e-d-c-b-c-d-e--
    # e-d-c-b-a-b-c-d-e
    # --e-d-c-b-c-d-e--
    # ----e-d-c-d-e----
    # ------e-d-e------
    # --------e--------
