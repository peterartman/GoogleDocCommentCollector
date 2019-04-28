from multiprocessing import Pool


def f(x):
    return x*x


p = Pool(10)
print(p.map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))