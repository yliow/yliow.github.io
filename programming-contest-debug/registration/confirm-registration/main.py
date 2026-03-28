import os
from pyutil import *
s = readfile('main0.tex')

name = 'Riley Salladay'
dir_ = name.replace(' ', '-')
os.system('rm -rf %s' % dir_)
os.system('mkdir %s' % dir_)
#os.system('cp thismyquiz.sty %s' % dir_)
#os.system('cp venmo_qrcode.pdf %s' % dir_)
regfee = 5.00
nummeals = 1
mealfee = nummeals * 5
tshirt = 20
total = regfee + mealfee + tshirt
for a,b in [('NAME', name),
            ('DATE', '9/28/2026'),
            ('EARLY', '11/31/2026'),
            ('REGFEE', r'\$%.2f' % regfee),
            ('NUMMEALS', nummeals),
            ('MEALFEE', r'\$%.2f' % mealfee),
            ('TSHIRT', r'\$%0.2f' % tshirt),
            ('TOTAL',  r'\$%0.2f' % total),
            ('EARLYDATE', r'11/30/2025'),
            ('DISCOUNTED', r'\$%0.2f' % (0.9 * total)),
            ]:
    s = s.replace(a, str(b))
writefile('%s/%s.tex' % (dir_, dir_), s)

s = readfile('makefile0')
t = name.replace(' ', '-')
s = s % (t,t,t,t)
writefile('%s/makefile' % dir_, s)
#os.system('make')
