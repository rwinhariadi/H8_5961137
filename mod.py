s = "Erwin"
a = [1,2,3]

def foo(arg):
    print(f'arg = {arg}')
class Foo:
    pass

if(__name__=='__main__'):
    print('Executing as standalone script')
    print(s)
    print(a)
    foo('quux')
    x = Foo()
    print(x)