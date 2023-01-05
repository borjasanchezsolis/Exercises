def main():
    x = int(input('Whats x? '))
    print('x squared is', square(x))


def square(n):
    return n * n   #or pow(n, 2)


main()