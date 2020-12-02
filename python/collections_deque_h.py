from collections import deque

def main():
    n = int(input())

    d = deque()

    # Perform append, pop, popleft and appendleft methods on an empty deque
    for _ in range(n):
        command = input().split()

        if command[0] == 'pop':
            d.pop()
        elif command[0] == 'popleft':
            d.popleft()
        elif command[0] == 'appendleft':
            d.appendleft(command[1])
        elif command[0] == 'append':
            d.append(command[1])
    
    result = ''

    if len(d) > 0:
        for i in d:
            result = result + i + ' '
    
    print(result)

if __name__ == '__main__':
    main()