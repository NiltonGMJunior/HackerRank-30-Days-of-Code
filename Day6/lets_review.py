if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        st = str(input())
        st1 = ''.join([char for index, char in enumerate(st) if index % 2 == 0])
        st2 = ''.join([char for index, char in enumerate(st) if index % 2 != 0])
        print("{} {}".format(st1, st2))
