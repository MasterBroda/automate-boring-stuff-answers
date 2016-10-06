def collatz(num):
    if num == 1:
        pass
    else:
        if num % 2 == 0:
            num = num // 2
            print num
            collatz(num)
        else:
            num = (num*3) + 1
            print num
            collatz(num)

if __name__ == '__main__':
    collatz(3)