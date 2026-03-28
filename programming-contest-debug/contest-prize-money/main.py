xs = []
def f(n):
    if n == 0 or n == 1: return 1
    else: return f(n - 1) + f(n - 2)

for n in range(7):
    xs.append(f(n))

M = 800
xs = xs[1:]
print(xs)
s = sum(xs) * 3
print(s)
f = M / s
print(f)
ys = [f * x for x in xs]
#print(ys)
ys = [round(y, 2)  for y in ys]
print("ys:", ys)
print("sum:", sum(ys))
print("3 * sum:", sum(ys) * 3)
#zs = [10, 15, 25, 40, 50, 100]
print(list(round(a/b, 2) for a,b in zip(ys[:-1], ys[1:])))
