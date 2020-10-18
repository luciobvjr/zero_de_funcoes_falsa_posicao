import timeit
start = timeit.timeit()

from math import fabs
a = float(input('Limite inferior do intervalo: '))
b = float(input('Limite superior do intervalo: '))
e = float(input('Tolerância: '))


def h(x):
    h = (x**3) - 3.5*x
    return h


k = 0

while True:
    m = (a*h(b) - b*h(a)) / (h(b) - h(a))
    if fabs(h(m)) < e:
        print()
        print('Valor da abcissa na interseção=', m)
        print('iterações=', k)
        break
    else:
        k += 1
        if h(m)*h(a) < 0:
            b = m
        else:
            a = m

end = timeit.timeit()
print('Tempo de execução:',end - start)