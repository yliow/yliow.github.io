import re
import datetime; NOW = datetime.datetime.now()
from pyutil import *
s = readfile('programming-contest/index.html')
lines = s.split('\n')
t = []
for line in lines:
    if line.startswith('Last update:'):
        line = 'Last update: %s' % NOW
    t.append(line)
s = '\n'.join(t)
writefile('programming-contest/index.html', s)
