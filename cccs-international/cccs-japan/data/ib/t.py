from pyutil import *
s = readfile('tmp')
xs = s.split('\n')
xs = [_ for _ in xs if _.strip() != '']
xs = [_.split('\t') for _ in xs]
xs = [_[:-1] + _[-1].split(", ") for _ in xs]
for x in xs:
    print(x)
    if len(x) != 4: print("ERROR")
#for x in xs:
#    print(x, '[%s]' % x[-1])
xs = [','.join(_) for _ in xs]
for x in xs:
    print(x)
