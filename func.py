"""simple ex(docstr)"""

def add(a,b):
    """Adds two numbers"""
    return sub(a, -b)


def sub(a, b):
    return a - b

def say_hello(first_name, last_name='', age=0):
    print(f'Hello {first_name} {last_name}. Your name is {age}')

def f():
    return 10, 20, 30, 40


def test_say_hello():
    say_hello('Paul','Ianas',36)
    say_hello('Paul')
    say_hello(last_name = 'Ianas', first_name = 'Paul')

    params1 = ['Paul', 'Ianas', 36]
    say_hello(*params1)

    params2 = {'first_name':'Paul', 'last_name':'Ianas', 'age':36}  #dictionar
    print(params2['first_name'])

    say_hello(**params2) # ** tine de sintaxa, nu de pointeri

    a, b, c, d = f()
    a, b, c, d = d, c, b, a
    print(a, b, c, d)

if __name__ == '__main__':
    print(__doc__)
    print(__name__)
    print(add.__doc__)

    while True:
        x = int(input('x='))
        y = int(input('y='))
        print(f'x + y = {add(x,y)}')
        print(f'x - y = {sub(x,y)}')
        if x == 0 and y == 0:
            break
    test_say_hello()

def sub(a, b):
    print('Celalalt sub')
    return a - b


print(f'x-y = {sub(x,y)}')
