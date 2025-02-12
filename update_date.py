import re
import datetime; NOW = datetime.datetime.now()
from pyutil import *
f = readfile('programming-contest.html')
lines = f.read()
lines = lines.split('\n')
t = []
for line in lines:
    if t.startswith('Last update:')
        t = 'Last update: %s' % NOW
    t.append(line)
f.write('\n'.join(t))
