from pyutil import *
from all import *

import sys
country = ' '.join(sys.argv[1:])
print("country:", country)

d0 = get_config(country)
d1 = [('{%s}' % a, b) for a,b in d0]
# [('{year}', year), ...
            
s = readfile('index.template.html')
for a, b in d1:
    print(a, b)
    s = s.replace(a, b)

t = country.lower()
t = t.replace(' ', '-')
writefile('cccs-%s.html' % t, s)
