def str_to_tuples(s):
    xs = [_ for _ in s.split('\n')]
    xs = [_ for _ in xs if _.strip() != '']
    xs = [_.split('=', 1) for _ in xs]
    def IFELSE(b, a, c):
        if b: return a
        else: return c
    for _ in xs:
        if len(_) != 2:
            print("len:", len(_))
            print("_", _)
            raise Exception
    xs = [(a, IFELSE('#' in b, b.split('#')[0], b)) for a,b in xs]
    xs = [(a.strip(), b.strip()) for a,b in xs]
    return xs

# welcome
s = r'''
Nepal=नमस्ते!
Japan=ようこそ!
South Korea=환영합니다!
China=欢迎!
India=स्वागतम्!
Vietnam=Chào mừng!
Malaysia=Selamat datang!
Thailand=ยินดีต้อนรับนะ!
Indonesia=Selamat datang!
Pakistan=خوش آمدید!
'''
welcome = dict(str_to_tuples(s))

# summary sheet
# WARNING: "=" is used to split "x=1" so cannot have "=" on the right. must split with parameter 1
s = r'''
Nepal=
Japan=The following is the <a href="https://yliow.github.io/cccs-international/cccs-japan/docs/cccs-japan-summary-sheet.pdf">summary sheet / 日本語訳付き概要シート</a> (PDF) and the <a href='https://yliow.github.io/cccs-international/cccs-japan/docs/cccs-japan-poster-3-upscale.pdf'>flyer / 日本語訳付きチラシ</a> (PDF). 
South Korea=The following is the <a href="https://yliow.github.io/cccs-international/cccs-south-korea/docs/cccs-south-korea-summary-sheet.pdf">summary sheet  / 한국어 번역이 포함된 개요서</a> (PDF).
China=The following is the <a href="https://yliow.github.io/cccs-international/cccs-china/docs/cccs-china-summary-sheet.pdf">summary sheet / 附中文翻译的项目简介</a> (PDF).
India=
Vietnam=
Malaysia=
Thailand=
Indonesia=
Pakistan=
'''
summarysheet = dict(str_to_tuples(s))



# adjecive
s = r'''
Nepal=Nepali
Japan=Japanese
South Korea=South Korean
China=Chinese
India=Indian
Vietnam=Vietnamese
Malaysia=Malaysian
Thailand=Thai
Indonesia=Indonesian
Pakistan=Pakistani
'''
country_adj = dict(str_to_tuples(s))


# f1 visa denial rate
s = r'''
Nepal      =81%
Japan      = 5%
South Korea= 7%
China      =16%
India      =61%
Vietnam    =13%
Malaysia   =12%
Thailand   =41%
Indonesia  =37%
Pakistan   =71%
'''
f1denial0 = dict(str_to_tuples(s))


s = r'''
year=2026
nextyear=2027
region=East Asia, Southeast Asia and South Asia
tuition0=$14,677                        # fall tuition
tuition1=$29,354                        # fall+spring tuition
tuition2=$33,992                        # fall+spring+summer tuition
book0=$240                              # fall books
book1=$480                              # spring books
book2=$720                              #fall+spring+summer books
housing0=$3,313                         # fall housing
housing1=$6,626                         # spring housing
housing2=$18,266                        # fall + spring + summer housing
food0=$2,700
food1=$5,400
food2=-
transportation0=$800
transportation1=$1,760
transportation2=$3,088
personal0=$2,240
personal1=$4,480
personal2=$8,928
loanfees0=$16
loanfees1=$32
loanfees2=$48
coa0=$24,066
coa1=$48,132
coa2=$65,042
banksdoubleroom=$2,841
hughesdoubleroom=$3,040
hugheshaven=$3,320
newhall=$3,637
cougarvillage=$3,735
'''

xs = str_to_tuples(s)

def get_config(country):
    xs.append(('country', country))
    xs.append(('countryadj', country_adj[country]))
    xs.append(('countryuppercase', country.upper()))
    xs.append(('countrylowercase', country.lower()))
    xs.append(('f1denial0', f1denial0[country]))
    xs.append(('welcome', welcome[country]))
    xs.append(('summarysheet', summarysheet[country]))
    
    #for x in xs: print(x)
    return xs
