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
import urics, courses


NOW = datetime.datetime.now()
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

    </style>
  </head>
    '''


def navigation_bar(name):
    if name == 'cccs':
        return '<a href="index.html">Home</a> | <a href="index.html">CCCS</a>'
    elif name == 'pics':
        return '<a href="index.html">Home</a> | Outreach'
    elif name == 'urics':
        return '<a href="index.html">Home</a> | URiCS'
    elif name == 'cs_day':
        return '<a href="index.html">Home</a> | CS Day'
    else:
        return '<a href="index.html">Home</a> [INCOMPLETE]'
    
def title(name):
    if name == 'cccs':
        return 'CCCS<br>Columbia College Computer Science'
    if name == 'cs_day':
        return 'CS Day'
    elif name == 'pics':
        return r'''
        <div style="display: flex; justify-content: center; background-color:rgba(0,65,122,255); padding:10px"><img src='images/pics/pics.png'/></div><br>
        Welcome to PiCS'''
    elif name == 'urics':
        return '''<div>
        URiCS <br>
        <div style="color:#D3D3D3;">Undergraduate Research in Computer Science</div>
        </div>'''
    else:
        return '[NO TITLE]'
    
#==============================================================================
# GENERAL HTML
#==============================================================================
def header(title):
    return r'<h1>%(title)s</h1>' % {'title':title}

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
Copyright Dr. Yihsiang Liow (yliow@ccis.edu | <a href='http://bit.ly/yliow0'>http://bit.ly/yliow0</a>)
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
    <li><a href="pics.html">pics ... test</a></li>
    </ul>

    '''

def tutorials():
    return r'''
        <h2><a id="tutorials">Tutorials</a> <a href="#top" style="font-size:16px">top</a></h2>

    <table border='1'>
      <tr>
        <td><a href='vmware/vmwareplayer.pdf'>vmwareplayer.pdf</a></td>
        <td>
          How to use the VMWare WorkStation or VMWare Player software.
          (The screenshots in the pdf are slightly different from the newer
          versions of the VMWare software.
          But in general, the process for using the software is the same.)
        </td>
      </tr>

      <tr>
        <td><a href='unix1-1/main.pdf'>unix1.pdf</a></td>
        <td>
          How to work with linux. Extra linux commands
          <a href="https://docs.google.com/document/d/1QivrEQChzKZb2RV5X0p-TbEWh65K_NR-shsmMWi5O_4/edit?usp=sharing">here</a>.
        </td>
      </tr>
      
      <tr>
        <td>
          <a href='xemacs/main.pdf'>emacs.pdf</a>
        </td>
        <td>
          How to use emacs/xemacs.
        </td>
      </tr>

      <tr>
        <td>
          <a href='gpp/main.pdf'>gpp.pdf</a>
        </td>
        <td>
          How to use g++ to compile C++ programs.
        </td>
      </tr>

      <tr>
        <td>
          <a href='make/main.pdf'>make.pdf</a>
        </td>
        <td>
          How to use make to automate building your programs.
        </td>
      </tr>

      <tr>
        <td>
          <a href='gdb/main.pdf'>gdb.pdf</a>
        </td>
        <td>
          How to use gdb to help find bugs.
        </td>
      </tr>
      
      <tr>
        <td>
          <a href='memory-debugging/main.pdf'>memory-debugging.pdf</a>
        </td>
        <td>
          How to use Google’s addr sanitizer and valgrind to find memory bugs.
        </td>
      </tr>

      <tr>
        <td>
          <a href='git/main.pdf'>git.pdf</a>
        </td>
        <td>
          How to use git and github.
        </td>
      </tr>

      <tr>
        <td>
          <a href='googletest/main.pdf'>googletest.pdf</a>
        </td>
        <td>
          How to use Google’s googletest to write C++ unit tests..
        </td>
      </tr>

      <tr>
        <td>
          <a href='static-analysis/main.pdf'>static-analysis.pdf</a>
        </td>
        <td>
          TO COME
        </td>
      </tr>

      <tr>
        <td>
          <a href=''>Helloweb1.pdf</a>
        </td>
        <td>
          How to create a basic website using pythonanywhere. (Moved to CISS430 notes.)
        </td>
      </tr>

      <tr>
        <td>
          <a href=''>sdl.pdf</a>
        </td>
        <td>
          How to install the SDL library. Required for CISS245.
          (REMOVED: SDL is now installed in our Fedora virtual machine.)
        </td>
      </tr>

      <tr>
        <td>
          <a href='latex/main.pdf'>latex.pdf</a>
        </td>
        <td>
          How to write LaTeX documents and generate pdf.
        </td>
      </tr>

      <tr>
        <td>
          <a href='latex-graph/main.pdf'>latex-graph.pdf</a>
        </td>
        <td>
          How to draw directed and undirected graphs (including DFAs, TMs).
        </td>
      </tr>

      <tr>
        <td>
          <a href='latex-automata/main.pdf'>latex-automata.pdf</a>
        </td>
        <td>
          How to draw automata diagram.
        </td>
      </tr>

      <tr>
        <td>
          <a href='latex-2d/main.pdf'>latex-2d-graphs.pdf</a>
        </td>
        <td>
          How to draw functions in 2D plane.
        </td>
      </tr>

      <tr>
        <td>
          <a href='latex-surfaces/main.pdf'>latex-surfaces.pdf</a>
        </td>
        <td>
          How to draw 3D surfaces. TO COME.
        </td>
      </tr>

      <tr>
        <td>
          <a href='book/book.tar.gz'>book.tar.gz</a>
        </td>
        <td>
          Book template.
        </td>
      </tr>
      
    </table>
    '''

def wanna_feed_your_brain():
    return '%s %s' % (section(name='Wanna feed your brain?', id_="wanna-feed-your-brain"),
                      ul(htmls=[quotes(),
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
        ul(htmls=[calendar(),
                  academic_calendar_final_exam(),
                  classes_for_current_semester(),
                  cs_hangout(),
                  publication_about_cccs(),
                  cs101(),
                  research(),
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

def pics():
    images_ = images(srcs_captions=[('images/pics/image16.png', 'HS Programming Contest #2 (2016)'),
                                    ('images/pics/image4.png', 'HS CS internship program (2016-2017)'),
                                    ('images/pics/image1.png', 'Weekend seminar (10/2016)'),
                                    ('images/pics/image7.png', 'Break during HS Programming Contest #1 (2015)'),
                                    ('images/pics/image14.png', 'Computer game contest during HS Programming Contest #2 (2016)'),

    ])
    return webpage(navigation_bar=navigation_bar('pics'),
                   header=header(title('pics')),
                   body=r'''
%(images)s
Welcome to PiCS (Portal into Computer Science), the computer science outreach programs of Columbia College (of Missouri).
<br><br>           
[PICS TO BE TRANSFERRED]
                   
<h2>Goal</h2>

The goal of PiCS is to introduce K-12 students to the exciting area of Computer Science.
We have visited Benton Elementary School and Alpha Hart Lewis Elementary School to talk about computer science and to teach basic programming.
In spring 2017 we organized an “Hour of Code” event for Jeff Middle School.
We have organized several high school events including an annual High School Programming Contest since spring 2015.
We are also organizing several summer camps for middle school and high school students.
More programs for elementary school students are forthcoming.

<h2>Students</h2>

Click on the following links to find out more about our programs and activities:
<ul>
<li><a href='https://docs.google.com/document/d/1weDfXSYzwsvBL-DvTmnb4SyOn_Rf1SKofbQoE4yN3fs/'>High school</a></li>
<li><a href='https://docs.google.com/document/d/1g7FxMLD8pBvVEF_tjj7fw7fCA8SqDPCPv5P438ePR04/'>Middle school</a></li>
<li>Elementary school [coming soon]</li>
</ul>
Here’s the <a href="http://bit.ly/pics-summer">2017 summer camps link</a>.

<h2>Teachers</h2>
If your school wishes to partner with Columbia College to promote computer science among your students, please email
Dr. Yihsiang Liow (<a href="mailto:yliow@ccis.edu">yliow@ccis.edu</a>).
We can for instance organize an “Hour of Code” for your school or classes.
Here’s our
<a href="https://photos.app.goo.gl/1BeGWgch3uMzWJmN7">“Hour of Code” event in 3/2017</a>.

<h2>“PiCS”?</h2>
The name PiCS and its logo (the spiral) were created by a group of our CS students, Mr. Nathaniel Graham, and Dr. Yihsiang Liow on 2015/03/30 while planning for the first High School Programming Contest (2015/04). Now they represent our outreach to all K-12 students. 

<h2>Donors and Sponsors</h2> 
To become a donor or sponsor of PiCS to support computer science outreach programs to K-12 students, please email
Dr. Yihsiang Liow (<a href="mailto:yliow@ccis.edu">yliow@ccis.edu</a>). All donors/sponsors (past, current, and recurring) are acknowledged below (except for anonymous donors).
<ul>
 <li>Columbia College of Missouri
 <li>MidwayUSA
 <li>Partner-in-Education (Dr. T. Vandover)
 <li>Julia Collins
</ul>
<br><br>
                   
<h2>Are you game?</h2>
To find out more, get in touch with Dr. Yihsiang Liow (<a href="mailto:yliow@ccis.edu">yliow@ccis.edu</a>) for a chat.
<a href="https://drive.google.com/file/d/1o1dJ6F0MmSsFW4PAKX94JrsSeGHJg6ND/view?usp=sharing">Why CS?</a> |
<a href="https://drive.google.com/file/d/0BzjYrK0VFuMWaXI1ZlJpNTkxT0U/view?resourcekey=0-JCm-tl5MEfX0peYxdfKOYA">CS program hunting</a>
                   ''' % {'images':images_})


def urics_():
    return webpage(navigation_bar=navigation_bar('urics'),
                   header=header(title('urics')),
                   body=urics.index()
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



if __name__ == '__main__':
    f = open('index.html', 'w'); f.write(cccs()); f.close()
    f = open('pics.html', 'w'); f.write(pics()); f.close()
    f = open('urics.html', 'w'); f.write(urics_()); f.close()
    f = open('cs_day.html', 'w'); f.write(cs_day_page()); f.close()
