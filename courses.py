def index():
    data = [('http://ciss145.pythonanywhere.com', 'CISS145 (Python)'),
            ('http://ciss170.pythonanywhere.com', 'CISS170 (Intro CIS)'),
            ('http://ciss176.pythonanywhere.com', 'CISS176 (Intro CS)'),
            ('http://ciss234.pythonanywhere.com', 'CISS234 (VB)'),
            ('http://ciss238.pythonanywhere.com', 'CISS238 (Java)'),
            ('http://ciss240.pythonanywhere.com', 'CISS240 (Intro Prog)'), 
            ('http://ciss245.pythonanywhere.com', 'CISS245 (Adv Prog)'), 
            ('http://ciss312.pythonanywhere.com', 'CISS312 (ACM)'),
            ('http://ciss350.pythonanywhere.com', 'CISS350 (Alg-1)'),
            ('http://ciss358.pythonanywhere.com', 'CISS358 (Alg-2)'),
            ('http://ciss360.pythonanywhere.com', 'CISS360 (Assembly)'),
            ('http://ciss362.pythonanywhere.com', 'CISS362 (Automata)'),
            ('http://ciss375.pythonanywhere.com', 'CISS375 (Compilers)'),
            ('http://ciss380.pythonanywhere.com', 'CISS380 (Graphics)'),
            ('http://ciss410.pythonanywhere.com', 'CISS410 (Ntwks)'),
            ('http://ciss430.pythonanywhere.com', 'CISS430 (DB)'),
            ('http://ciss438.pythonanywhere.com', 'CISS438 (OOAD)'),
            ('http://ciss445.pythonanywhere.com', 'CISS445 (PL)'),
            ('http://ciss450.pythonanywhere.com', 'CISS450 (AI)'),
            ('http://ciss451.pythonanywhere.com', 'CISS451 (Crypto)'),
            ('http://ciss465.pythonanywhere.com', 'CISS465 (SE)'),
            ('http://ciss494.pythonanywhere.com', 'CISS493/4 (Senior sem)'),
            ('http://math325.pythonanywhere.com', 'MATH325 (DM 2)'),
            ('http://ciss999.pythonanywhere.com', 'Computer vision (COMING)'),
            ('http://ciss998.pythonanywhere.com', 'Qt (COMING)'),
        ]
    #print(data[0][0][7:14]) -- sort key
    data.sort(key=lambda x: x[0][7:14])
    #for x in data: print(x)
    html = r'''<h2><a id="courses">Courses</a> <a href="#top" style="font-size:16px">top</a></h2>
In the future all my notes will be public. Right now they are all under heavy construction.
<ul>'''
    for url, s in data:
        html += '<li>xxx<a href="%s">%s</a>' % (url, s)
    html += '</ul>'
    return html

    # DEPRECATED
    return \
    r'''<h2><a id="courses">Courses</a> <a href="#top" style="font-size:16px">top</a></h2>
    In the future all my notes will be public. Right now they are all under heavy construction.
    <ul>
    <li><a href="http://ciss145.pythonanywhere.com">CISS145 (Python)</a>
    <li><a href="http://ciss170.pythonanywhere.com">CISS170 (Intro CIS)</a>
    <li><a href="http://ciss176.pythonanywhere.com">CISS176 (Intro CS)</a>
    <li><a href="http://ciss234.pythonanywhere.com">CISS234 (VB)</a>
    <li><a href="http://ciss238.pythonanywhere.com">CISS238 (Java)</a>
    <li><a href="http://ciss240.pythonanywhere.com">CISS240 (Intro Prog)</a> 
    <li><a href="http://ciss245.pythonanywhere.com">CISS245 (Adv Prog)</a> 
    <li><a href="http://ciss312.pythonanywhere.com">CISS312 (ACM)</a>
    <li><a href="http://ciss350.pythonanywhere.com">CISS350 (Alg-1)</a>
    <li><a href="http://ciss358.pythonanywhere.com">CISS358 (Alg-2)</a>
    <li><a href="http://ciss360.pythonanywhere.com">CISS360 (Assembly)</a>
    <li><a href="http://ciss362.pythonanywhere.com">CISS362 (Automata)</a>
    <li><a href="http://ciss375.pythonanywhere.com">CISS375 (Compilers)</a>
    <li><a href="http://ciss380.pythonanywhere.com">CISS380 (Graphics)</a>
    <li><a href="http://ciss410.pythonanywhere.com">CISS410 (Ntwks)</a>
    <li><a href="http://ciss430.pythonanywhere.com">CISS430 (DB)</a>
    <li><a href="http://ciss438.pythonanywhere.com">CISS438 (OOAD)</a>
    <li><a href="http://ciss445.pythonanywhere.com">CISS445 (PL)</a>
    <li><a href="http://ciss450.pythonanywhere.com">CISS450 (AI)</a>
    <li><a href="http://ciss451.pythonanywhere.com">CISS451 (Crypto)</a>
    <li><a href="http://ciss465.pythonanywhere.com">CISS465 (SE)</a>
    <li><a href="http://ciss494.pythonanywhere.com">CISS493/4 (Senior sem)</a>
    <li><a href="http://math325.pythonanywhere.com">MATH325 (DM 2)</a>
    <li><a href="http://ciss999.pythonanywhere.com">Computer vision (COMING)</a>
    <li><a href="http://ciss998.pythonanywhere.com">Qt (COMING)</a>
    </ul>
'''

index()
