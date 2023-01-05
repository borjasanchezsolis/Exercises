def hello(to='world'):
    print('hello,', to)


hello()
name = input('Whats your name? ').strip().title()
hello(name)