
if __name__ == '__main__':

    phonebook = {}

    n = int(input())

    for i in range(n):
        inp = list(map(str, input().split()))
        phonebook[inp[0]] = inp[1]

    while True:
        try:
            inp = str(input())
        except EOFError:
            break
            
        if inp in phonebook:
            print(inp + '=' + phonebook[inp])
        else:
            print('Not found')
