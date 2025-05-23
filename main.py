"""
webpage structure

<html>

  %(head)s

  <body style="font-family:arial; margin:200px; padding:200px; ">
    
    %(navigation_bar)s

    %(header)s

    <h2>%(title)s</h2>
    
    <hr>

    %(body)s

  </body>
</html>
"""

import datetime
from html_util import *
from html_fragments import *
import urics, courses, quotes, pics
import why_you_should_still_consider_cs, highschool
import cccsdiscord
import how_to_give_a_talk
NOW = datetime.datetime.now()
CURR_YEAR = NOW.year
HEAD = r'''
    <head>
    <style>

      * {
          box-sizing: border-box;
      }
      
      .row {
          display: flex;
      }
      
      /* Create three equal columns that sits next to each other */
      .column {
          flex: 33.33%;
          padding: 5px;
      }
      
      table {
          font-family: arial, sans-serif;
          border: 1px solid black;
          border-collapse: collapse;
          width: 100%;
      }

      td, th {
          text-align: left;
          vertical-align:top;
          padding: 8px;
      }

    <!-- vertically stacked images -->

.detailImgWrapper
    {
    display: inline;
    display: block;
    width: 100px;
    padding: 0;
    float: right;
    margin: 0 0 0 15px;
    }

    </style>
  </head>
    '''

def writefile(filename, s):
    f = open(filename, 'w'); f.write(s); f.close()
    
def navigation_bar(name):
    home = '<a href="index.html">Home</a>'
    cccs = '<a href="index.html">CCCS</a>'
    outreach = 'Outreach'
    urics = 'URiCS'
    quotes = 'Quotes'
    cs_day = 'CS Day'
    cccsdiscord = 'CCCS Discord'
    highschool = 'High school CS'
    q_and_a = 'Q&A'
    how_to_give_a_talk = 'How to give a talk'
    def join(xs): return ' | '.join(xs)

    d = {'cccs':   [home, cccs],
         'pics':   [home, cccs, outreach],
         'urics':  [home, cccs, urics],
         'quotes': [home, cccs, quotes],
         'cs_day': [home, cccs, cs_day],
         'cccsdiscord': [home, cccs, cccsdiscord],
         'why_you_should_still_consider_cs': [home, cccs, outreach, highschool, q_and_a],
         'how_to_give_a_talk': [home, cccs, how_to_give_a_talk],

         }
    return join(d.get(name, [home, cccs] + ['?']))
    
def title(name):
    if name == 'cccs':
        return 'CCCS<br>Columbia College Computer Science'
    if name == 'cs_day':
        return 'CS Day'
    elif name == 'pics':
        return r'''
        <div style="display: flex; justify-content: center; background-color:rgba(0,65,122,255); padding:10px"><img src='images/pics/pics.png'/></div><br>
        Welcome to PiCS'''
    elif name == 'highschool':
        return r'''
        <div style="display: flex; justify-content: center; background-color:rgba(0,65,122,255); padding:10px"><img src='images/pics/pics.png'/></div><br>
        High School CS'''
    elif name == 'urics':
        return '''<div>
        URiCS <br>
        <div style="color:#D3D3D3;">Undergraduate Research in Computer Science</div>
        </div>'''
    elif name == 'quotes':
        return '''<div>
        Quotes 
        </div>'''
    elif name == 'cccsdiscord':
        return '''<div>
        CCCS Discord 
        </div>'''
    elif name == 'how_to_give_a_talk':
        return '''<div>
        How to give a talk
        </div>'''
    elif name == 'why_you_should_still_consider_cs':
        return '''<div>
        Why you should still consider CS even though it’s tough and you might get a lower GPA than another major
        </div>'''
    else:
        return '[NO TITLE]'
    
#==============================================================================
# GENERAL HTML
#==============================================================================
def header(title):
    return r'''
<h1>%(title)s</h1>
    '''% {'title':title}

def tablerow(link, name, description):
    return '<tr><td><a href="%(link)s">%(name)s</td><td>%(description)s</td></tr>' % \
        {'link':link, 'name':name, 'description':description}


def section(name='Useful stuff', id_='useful_stuff'):
    return r'''<h2><a id="%(id_)s">%(name)s</a> <a href="#top" style="font-size:16px">top</a></h2>''' % \
        {'name':name,
         'id_':id_,
         }

def webpage(head=HEAD,
            navigation_bar='',
            header='',
            body=''):
    return r'''
<html>  
%(head)s
<body style="font-family: arial; margin-left:100px; margin-right:100px; ">
%(navigation_bar)s
%(header)s
<h2>%(title)s</h2><hr>
%(body)s
<br>
<hr>
&copy Copyright 2013-%(curr_year)s. Yihsiang Liow. All rights reserved. (yliow@ccis.edu
    | <a href='http://yliow.github.io'>http://yliow.github.io</a>
    | <a href='http://bit.ly/yliow0'>http://bit.ly/yliow0</a>)
<br>
Last update: %(now)s
</body>
</html>
    ''' % {'head':head,
           'navigation_bar':navigation_bar,
           'title':title,
           'header':header,
           'body':body,
           'now':NOW,
           'curr_year':CURR_YEAR,
           }


    

def toc():
    return r'''
    <h2><a id="top">TOC</a></h2>
    <ul>
      <li><a href="#useful_stuff">Useful stuff</a></li>
      <li><a href="#events_t_shirts_etc">Events, T-shirts, etc.</a></li>
      <li><a href="#outreach">Outreach</a></li>
      <li><a href="#others">Others</a></li>      
      <li><a href="#software">Software</a></li>      
      <li><a href="#courses">Courses</a></li>      
      <li><a href="#tutorials">Tutorials</a></li>
      <li><a href="#wanna-feed-your-brain">Wanna feed your brain?</a></li>
    <li><a href="pics.html">K-12</a> | <a href="highschool.html">HS</a></li>
    </ul>

    '''

def tutorials():
    def tr(path, name, comment):
        return r"<tr><td><a href='%(path)s'>%(name)s</a></td><td>%(comment)s</td></tr>" % {'path':path,
                                                                                           'name':name,
                                                                                           'comment':comment}
        
    html = r'''
        <h2><a id="tutorials">Tutorials</a> <a href="#top" style="font-size:16px">top</a></h2>
    <table border='1'>
    '''
    data = [('pdfs/vmware/vmwareplayer.pdf',
             'vmwareplayer.pdf',
             '''How to use the VMWare WorkStation or VMWare Player software.
             (The screenshots in the pdf are slightly different from the newer
             versions of the VMWare software.
             But in general, the process for using the software is the same.)'''),
            ('pdfs/unix1-1/main.pdf',
             'unix1.pdf',
             '''How to work with linux. Extra linux commands
             <a href="https://docs.google.com/document/d/1QivrEQChzKZb2RV5X0p-TbEWh65K_NR-shsmMWi5O_4/edit?usp=sharing">here</a>'''),
            ('pdfs/unix1-1-python/main.pdf',
             'unix1.pdf (python version)',
             '''This is the python version of unix1.pdf.'''),
            ('pdfs/xemacs/main.pdf',
             'emacs.pdf', 
             'How to use emacs/xemacs.'),
            ('pdfs/xemacs-python/main.pdf',
             'emacs.pdf (python version)', 
             'This is the python version of emacs.pdf.'),
            ('pdfs/gpp/main.pdf',
             'gpp.pdf', 
             'How to use g++ to compile C++ programs.'),
            ('pdfs/make/main.pdf',
             'make.pdf', 
             'How to use make to automate building your programs.'),
            ('pdfs/gdb/main.pdf',
             'gdb.pdf',
             'How to use gdb to help find bugs.'),
            ('pdfs/memory-debugging/main.pdf',
             'memory-debugging.pdf',
             'How to use Google’s addr sanitizer and valgrind to find memory bugs.'),
             ('pdfs/git/main.pdf',
              'git.pdf',
              'How to use git and github.'),
             ('pdfs/googletest/main.pdf',
              'googletest.pdf', 
              'How to use Google’s googletest to write C++ unit tests.'),
             ('pdfs/static-analysis/main.pdf',
              'static-analysis.pdf',
              'TO COME'),
             ('',
              'Helloweb1.pdf', 
              'How to create a basic website using pythonanywhere. (Moved to CISS430 notes.)'),
             ('',
              'sdl.pdf', 
              '''How to install the SDL library.
                 Required for CISS245.
                 (REMOVED: SDL is now installed in our Fedora virtual machine.)'''),
             ('pdfs/latex/main.pdf',
              'latex.pdf', 
              'How to write LaTeX documents and generate pdf.'),
             ('pdfs/latex-graph/main.pdf',
              'latex-graph.pdf', 
              'How to draw directed and undirected graphs (including DFAs, TMs).'),
             ('pdfs/latex-automata/main.pdf',
              'latex-automata.pdf',
              'How to draw automata diagram.'),
             ('pdfs/latex-2d/main.pdf',
              'latex-2d-graphs.pdf', 
              'How to draw functions in 2D plane.'),
             ('pdfs/latex-surfaces/main.pdf',
              'latex-surfaces.pdf', 
              'How to draw 3D surfaces. TO COME.'),
             ('pdfs/graphviz/main.pdf',
              'graphviz.pdf', 
              'How to draw directed/undirected3 graphs using graphviz.'),
             ('book/book.tar.gz',
              'book.tar.gz',
              'Book template.'),
             ('article/article.tar.gz',
              'article.tar.gz',
              'Article template.'),
    ]

    for path,name,comment in data:
        html += tr(path=path, name=name, comment=comment)
    html = html + '</table>'
    return html

def wanna_feed_your_brain():
    return '%s %s' % (section(name='Wanna feed your brain?', id_="wanna-feed-your-brain"),
                      ul(htmls=['<a href="quotes.html">Quotes</a>',
                                '<a href="https://docs.google.com/document/d/1taIWv3QzXe1WKmqW2DvG_FYNiHtSLcFisZqz1tolM4M/">Yes</a> | No – not clickable']))

def cccs():
    return webpage(navigation_bar=navigation_bar('cccs'),
                   header=header(title('cccs')),
                   body=r'''
    I'm in the process of moving <a href="http://bit.ly/yliow0">http://bit.ly/yliow0</a> to this website.    
    Let me know if there are broken links.

    <!-- pictures -->
    <div class="row">
      <div class="column">
        <img src="images/midway-reduce10.jpg" style="width:100%%">
      </div>
      <div class="column">
        <img src="images/dinner0-reduce10.jpg" style="width:100%%">
      </div>
    <div class="column">
    <img src="images/dinner1-reduce10.jpg" style="width:100%%">
      </div>
    </div>

    %(toc)s
    
    <hr>                   
    %(useful_stuff)s
    %(events_t_shirts_etc)s
    %(outreach)s
    %(others)s
    %(software)s
    %(courses)s
    %(tutorials)s
    %(wanna_feed_your_brain)s 
    ''' % {
        'toc':toc(),
        'useful_stuff':useful_stuff(),
        'events_t_shirts_etc':events_t_shirts_etc(),
        'outreach':outreach(),
        'others':others(),
        'software':software(),
        'tutorials':tutorials(),
        'wanna_feed_your_brain':wanna_feed_your_brain(),
        'courses':courses.index(),
    })


def useful_stuff():
    return r"""<img style="float:right; padding:20px 20px 20px 20px; width:25%" src='images/graph2.png'/>""" +\
        section(name='Useful stuff', id_='useful_stuff') + \
        ul(htmls=["<a href='bugs/index.html'>Bugs</a> [NEW]",
                  calendar(),
                  academic_calendar_final_exam(),
                  "Get in touch <ul> <li>%s <li>%s </ul>" % (cccs_discord(), cccs_google_group()),
                  cs101(),
                  classes_for_current_semester(),
                  cs_hangout(),
                  publication_about_cccs(),
                  companies(),
                  #reu(),
                  research(),
                  administrative_stuff(),
        ])

def events_t_shirts_etc():
    return \
        r"""<img style="float:right; padding:20px 20px 20px 20px; width:25%" src='images/graph1.png'/>""" +\
        section(name='Events, T-shirts, etc.', id_='events_t_shirts_etc') + \
        ul(htmls=[pictures_and_videos(),
                  cs_club(),
                  cs_day(),
                  cs_jam(),
                  department_welcome_lunch(),
                  end_of_semester_presentations(),
                  end_of_semester_celebration(),
                  facebook(),
                  game_tournaments(),
                  industrial_connection(),
                  kickoff(),
                  media_committee(),
                  movie_night(),
                  monday_programming_challenges(),
                  robotics_group(),
                  t_shirt(),
                  programming_contest(),
                  high_school_programming_contest(),
        ])

def outreach():
    return section(name='Outreach', id_='outreach') + \
        ul(htmls=['US students: Local high schools | Hannibal | State Tech',
                  "International students: <a href='https://docs.google.com/document/d/1rJRVfzMLUaOJs5R7oF0y3-gHf68EmERlXfZlvJtdfAQ/edit#'>Nepal</a> | <a href='https://docs.google.com/document/d/1regRPe9dhVKWgKY2iJ59YW_S2venGytsSuiWh2FSUrw/edit'>Committee</a>",
                  ])


def software():
    return r'''<h2><a id="software">Software</a> <a href="#top" style="font-size:16px">top</a></h2>
<ul>
    <li>Software downloads for classes:
    <a href="https://docs.google.com/document/d/1KFeT4hDx6HoaNM7qZSyVf0RY6wYwvX83PZ-wZY5x2oo/edit?usp=sharing">README</a>
    (<a href="https://docs.google.com/document/d/1gsozRu7xMSO0WO_QouY81B5WeDt2Sg119JTF9I1Mq2Q/edit?usp=sharing">README</a> backup)
    |
    <a href="https://drive.google.com/drive/folders/0B7Sweg7OrVSTQUh6a0VmVnMzVm8">Software folder</a></li>
    <li>Link for SDL <a href="https://drive.google.com/file/d/1munqhXWCN3J3Wp_0GtrvxZozGPwj7JiQ/view?usp=sharing">demo.tar</a>
    (for CISS245 game development)</li>
    <li>Web-based</li>
    <ul>
        <li>C++: <a href="https://repl.it/languages/cpp">repl-c++</a> | <a href="http://cpp.sh/">cpp-sh</a></li>
        <li>Python2: <a href="http://colab-py2">colab-py2</a> | <a href="https://repl.it/languages/python">repl-python</a></li>
        <li>Python3: <a href="https://repl.it/languages/python3">repl-py3</a></li>
        <li>OCAML: <a href="https://try.ocamlpro.com/">ocamlpro</a></li>
        <li>SQL: <a href="https://dbfiddle.uk/">db fiddle</a></li>
        <li>PDF: <a href="http://www.xodo.com">xodo</a></li>
        <li>LaTeX: Some latex tutorials are below in the “Tutorials” section.</li>
        <ul>
            <li><a href="https://detexify.kirelabs.org/classify.html">handwriting-to-latex</a></li>
            <li>online latex: <a href="https://www.overleaf.com/">overleaf</a> | <a href="https://latexbase.com/">latexbase</a></li>
        </ul>
        <li><a href="https://sagecell.sagemath.org/">SageMath</a> (for research in math, cryptography, etc.)
    </ul>
</ul>
    '''

def others():
    return '%s %s' % (section(name='Others', id_='others'),
                      ul(htmls=[work_study(), cctt()]),
                      )

def images(float='right', srcs_captions='', width=r'33%'):
    s = ''
    for src,caption in srcs_captions:
        t = r'''<tr>
    <td><img width="100%%" src="%(src)s"/>
    <div style="font-size:12px; text-align:center; padding:5px">%(caption)s</div>
    </td>
  </tr>''' % {'src':src,'caption':caption}
        s += t
    html = r'''<div style="float:%(float)s; padding:20px 20px 20px 20px; width:%(width)s">
  <table style='border-collapse:collapse; border:none'>
    %(rows)s
  </table>
</div>''' % {'width':width, 'rows':s, 'float':float}
    print("\nhtml:", html)
    
    return html

def pics_():
    images_ = images(srcs_captions=[('images/pics/image16.png', 'HS Programming Contest #2 (2016)'),
                                    ('images/pics/image4.png',  'HS CS internship program (2016-2017)'),
                                    ('images/pics/image1.png',  'Weekend seminar (10/2016)'),
                                    ('images/pics/image7.png',  'Break during HS Programming Contest #1 (2015)'),
                                    ('images/pics/image14.png', 'Computer game contest during HS Programming Contest #2 (2016)'),

    ])
    return webpage(navigation_bar=navigation_bar('pics'),
                   header=header(title('pics')),
                   body=pics.index() % {'images':images_})


def pics_():
    images_ = images(srcs_captions=[('images/pics/image16.png', 'HS Programming Contest #2 (2016)'),
                                    ('images/pics/image4.png',  'HS CS internship program (2016-2017)'),
                                    ('images/pics/image1.png',  'Weekend seminar (10/2016)'),
                                    ('images/pics/image7.png',  'Break during HS Programming Contest #1 (2015)'),
                                    ('images/pics/image14.png', 'Computer game contest during HS Programming Contest #2 (2016)'),

    ])
    return webpage(navigation_bar=navigation_bar('pics'),
                   header=header(title('pics')),
                   body=pics.index() % {'images':images_})

def highschool_():
    return webpage(navigation_bar=navigation_bar('highschool'),
                   header=header(title('highschool')),
                   body=highschool.index()
)

def urics_():
    return webpage(navigation_bar=navigation_bar('urics'),
                   header=header(title('urics')),
                   body=urics.index()
)

def quotes_():
    return webpage(navigation_bar=navigation_bar('quotes'),
                   header=header(title('quotes')),
                   body=quotes.index() % {}
)

def why_you_should_still_consider_cs_():
    s = why_you_should_still_consider_cs.index()
    return webpage(navigation_bar=navigation_bar('why_you_should_still_consider_cs'),
                   header=header(title('why_you_should_still_consider_cs')),
                   body=s
)
    
def cs_day_page():
    return webpage(navigation_bar=navigation_bar('cs_day'),
                   header=header(title('cs_day')),
                   body=r'''
<a href="https://drive.google.com/drive/folders/1-C8w2Xqcpk-MXWBsp2CLb5DgCu1BApy5?usp=sharing">For committee</a>
                   
<h2>Fall 2022</h2>
<a href='https://photos.app.goo.gl/zpLQkxcUuANKa4AZ8'>https://photos.app.goo.gl/zpLQkxcUuANKa4AZ8</a><br>
WHAT: CS Day #2 <a href="https://docs.google.com/document/d/1fq1jV49gD7OpMiNWfYZnO0LffOibGSdHP4EXPi8FPPQ/edit#heading=h.e76ogupi6d86">Flyer</a>  <a href="https://docs.google.com/forms/d/e/1FAIpQLSeynMah_RXTMjvg3T0HRTLw5CT7bJXyyp0-T3FVj4TLlIaOlg/viewform?usp=sharing">RSVP link</a> (optional)<br>
WHEN: Monday 10/24, 5PM-6:30PM<br>
WHERE: Buchanan Hall, Room 107 (BUH107) https://www.ccis.edu/about/map</br> 
WHO: Anyone interested in finding out more about CS</br>
<br>
                   
<center>
What is CS?<br>
What is programming?<br>
Why is CS fun?<br>
What are career paths in CS?<br>
How to be successful in CS?<br>
Q&A<br>
</center>
<h2>Fall 2021</h2>

'''
    )

def cccsdiscord_():

    images_ = images(
        srcs_captions=[
            ('images/pics/image16.png', 'HS Programming Contest #2 (2016)'),
            ('images/pics/image4.png',  'HS CS internship program (2016-2017)'),
            ('images/pics/image1.png',  'Weekend seminar (10/2016)'),
            ('images/pics/image7.png',  'Break during HS Programming Contest #1 (2015)'),
            ('images/pics/image14.png', 'Computer game contest during HS Programming Contest #2 (2016)'),
            ])

    return webpage(navigation_bar=navigation_bar('cccsdiscord'),
                   header=header(title('cccsdiscord')),
                   body=cccsdiscord.index() # % {'images':''}
    )


def how_to_give_a_talk_():

    return webpage(navigation_bar=navigation_bar('how_to_give_a_talk'),
                   header=header(title('how_to_give_a_talk')),
                   body=how_to_give_a_talk.index() # % {'images':''}
    )


if __name__ == '__main__':
    writefile(filename='index.html',                            s=cccs())
    writefile(filename='pics.html',                             s=pics_())
    writefile(filename='highschool.html',                       s=highschool_())
    writefile(filename='urics.html',                            s=urics_())
    writefile(filename='cs_day.html',                           s=cs_day_page())
    writefile(filename='quotes.html',                           s=quotes_())
    writefile(filename='why_you_should_still_consider_cs.html', s=why_you_should_still_consider_cs_())
    writefile(filename='cccsdiscord.html',                      s=cccsdiscord_())
    writefile(filename='how_to_give_a_talk.html',               s=how_to_give_a_talk_())
    

