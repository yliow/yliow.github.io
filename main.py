"""
webpage structure

<html>  
  %(head)s
  <body style="font-family: arial">
    
    %(navigation_bar)s
    %(header)s
    <h2>%(title)s</h2>
    
    <hr>

    %(body)s
  </body>
</html>

"""
import datetime
LINKS = {'ciss145':'<a href="http://ciss145.pythonanywhere.com">CISS145 (Python)</a>'
         }

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
        return '<a href="">Home</a> | <a href="index.html">CCCS</a>'
    elif name == 'pics':
        return '<a href="">Home</a> | <a href="index.html">Outreach</a>'

def title(name):
    if name == 'cccs':
        return 'CCCS<br>Columbia College Computer Science'
    elif name == 'pics':
        return 'Welcome to PiCS'
    
def header(title):
    return r'<h1>%(title)s</h1>[Last update: %(now)s]' % {'title':title,'now':NOW}

def tablerow(link, name, description):
    return '<tr><td><a href="%(link)s">%(name)s</td><td>%(description)s</td></tr>' % \
        {'link':link, 'name':name, 'description':description}


def section(name):
    pass

def webpage(head=HEAD,
            navigation_bar='',
            header='',
            body=''):
    return r'''
<html>  
  %(head)s
  <body style="font-family: arial">
    
    %(navigation_bar)s
    %(header)s
    <h2>%(title)s</h2>
    
    <hr>

    %(body)s
  </body>
</html>
    ''' % {'head':head,
           'navigation_bar':navigation_bar,
           'title':title,
           'header':header,
           'body':body,
           }

def toc():
    return r'''
    <h2><a id="top">TOC</a></h2>
    <ul>
      <li><a href="#others">Others</a></li>      
      <li><a href="#software">Software</a></li>      
      <li><a href="#courses">Courses</a></li>      
      <li><a href="#tutorials">Tutorials</a></li>
      <li><a href="#wanna-feed-your-brain">Wanna feed your brain?</a></li>      
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
    return r'''
        <h2><a id="wanna-feed-your-brain">Wanna feed your brain?</a> <a href="#top" style="font-size:16px">top</a></h2>
    <ul>
      <li><a href="https://docs.google.com/document/d/1i4HYMQqOo0yP3XPTdtZqws2SgaJ71n2ikBd68c8FYig/edit">Quotes</a></li>
      <li><a href="https://docs.google.com/document/d/1taIWv3QzXe1WKmqW2DvG_FYNiHtSLcFisZqz1tolM4M/">Yes</a> | No – not clickable </li>
    </ul>
    '''


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
    %(others)s
    %(software)s
    %(courses)s
    %(tutorials)s
    %(wanna_feed_your_brain)s 
    ''' % {
        'toc':toc(),
        'others':others(),
        'software':software(),
        'tutorials':tutorials(),
        'wanna_feed_your_brain':wanna_feed_your_brain(),
        'courses':courses(),
    })

def courses():
    return r'''<h2><a id="courses">Courses</a> <a href="#top" style="font-size:16px">top</a></h2>
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
    <li><a href="http://ciss999.pythonanywhere.com">Computer vision</a>
    <li><a href="http://ciss998.pythonanywhere.com">Qt</a>
    </ul>
'''

def software():
    return r'''<h2><a id="software">Software</a> <a href="#top" style="font-size:16px">top</a></h2>
<ul>
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
    <li>Software downloads for classes:
    <a href="https://docs.google.com/document/d/1KFeT4hDx6HoaNM7qZSyVf0RY6wYwvX83PZ-wZY5x2oo/edit?usp=sharing">README</a>
    (<a href="https://docs.google.com/document/d/1gsozRu7xMSO0WO_QouY81B5WeDt2Sg119JTF9I1Mq2Q/edit?usp=sharing">README</a> backup)
    |
    <a href="https://drive.google.com/drive/folders/0B7Sweg7OrVSTQUh6a0VmVnMzVm8">Software folder</a></li>
    <li>Link for SDL <a href="https://drive.google.com/file/d/1munqhXWCN3J3Wp_0GtrvxZozGPwj7JiQ/view?usp=sharing">demo.tar</a>
    (for CISS245 game development)</li>
</ul>
    '''


def others():
    return r'''
    <h2><a id="others">Others</a> <a href="#top" style="font-size:16px">top</a></h2>
    <ul>
    <li><a href="https://docs.google.com/document/d/1nYQtW3TTPIAYHcOeU-KSe2aEOiWHZgn6LA9aybH8pw0/edit?usp=sharing">Work study</a>
    [only work study students have access]</li>
    <li><a href="http://cctt0.pythonanywhere.com/">Royal Ping Pong Club</a></li>
    </ul>
    '''


    
def pics():
    return webpage('pics', '')
    
if __name__ == '__main__':
    f = open('index.html', 'w'); f.write(cccs()); f.close()
    f = open('pics.html', 'w'); f.write(pics()); f.close()
