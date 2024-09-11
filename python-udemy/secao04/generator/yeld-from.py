def gen1():
    print('COMEÇOU GEN1')
    yield 1
    yield 2
    yield 3
    print('ACABOU GEN1')

def gen3():
    print('COMEÇOU GEN3')
    yield from gen1()
    yield 4
    yield 5
    yield 6
    print('ACABOU GEN3')

def gen2(gen=None):
    print('COMEÇOU GEN 2')
    if gen is not None:
        yield from gen()
    yield 7
    yield 8
    yield 9
    print('ACABOU GEN 2')

seq = gen2()


for n in seq:
    print(n)

