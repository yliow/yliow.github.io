from pyutil import *
s = readfile('index.template.html')

year = '2026'
nextyear = '2027'
country = 'Japan'
country_adj = 'Japanese'
country_uppercase = country.upper()
country_lowercase = country.lower()
region = 'East Asia'
tuition0 = '$14,677' # fall tuition
tuition1 = '$29,354' # fall+spring tuition
tuition2 = '$33,992' # fall+spring+summer tuition
book0 = '$240'
book1 = '$480'
book2 = '$720'
housing0 = '$3,313'
housing1 = '$6,626'
housing2 = '$18,266'
food0 = '$2,700'
food1 = '$5,400'
food2 = '-'
transportation0 = '$800'
transportation1 = '$1,760'
transportation2 = '$3,088'
personal0 = '$2,240'
personal1 = '$4,480'
personal2 = '$8,928'
loanfees0 = '$16'
loanfees1 = '$32'
loanfees2 = '$48'
coa0 = '$24,066'
coa1 = '$48,132'
coa2 = '$65,042'
banksdoubleroom = '$2,841'
hughesdoubleroom = '$3,040'
hugheshaven = '$3,320'
newhall = '$3,637'
cougarvillage = '$3,735'

for a, b in [('{year}', year),
             ('{nextyear}', nextyear),
             ('{country}', country),
             ('{country-adj}', country_adj),
             ('{country-uppercase}', country_uppercase),
             ('{country-lowercase}', country_lowercase),
             ('{region}', region),
             ('{tuition0}', tuition0),
             ('{tuition1}', tuition1),
             ('{tuition2}', tuition2),
             ('{book0}', book0),
             ('{book1}', book1),
             ('{book2}', book2),
             ('{housing0}', housing0),
             ('{housing1}', housing1),
             ('{housing2}', housing2),
             ('{food0}', food0),
             ('{food1}', food1),
             ('{food2}', food2),
             ('{transportation0}', transportation0),
             ('{transportation1}', transportation1),
             ('{transportation2}', transportation2),
             ('{personal0}', personal0),
             ('{personal1}', personal1),
             ('{personal2}', personal2),
             ('{loanfees0}', loanfees0),
             ('{loanfees1}', loanfees1),
             ('{loanfees2}', loanfees2),
             ('{coa0}', coa0),
             ('{coa1}', coa1),
             ('{coa2}', coa2),
             ('{banksdoubleroom}', banksdoubleroom),
             ('{hughesdoubleroom}', hughesdoubleroom),
             ('{hugheshaven}', hugheshaven),
             ('{newhall}', newhall),
             ('{cougarvillage}', cougarvillage),
             ]:
    print(a, b)
    b = '[[[%s]]]' % b # for testing purposes
    s = s.replace(a, b)

writefile('aaa.html', s)

