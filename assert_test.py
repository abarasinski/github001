import sys

def f(x):
    assert x < 0, 'x musi być ujemne'
    return x ** 2

print(f(int(sys.argv[1])))
