def header():
    return r'''
        <h1>Y. Liow (under heavy construction)</h1>

    I'm in the process of moving <a href="http://bit.ly/yliow0">http://bit.ly/yliow0</a> to this website.
    
    Let me know if there are broken links.

    <br><br>
    NOTE: Ctrl+Shift+R to do a hard reload of the page in case your browser is using a stale cached page.

    <!-- pictures -->
    <div class="row">
      <div class="column">
        <img src="images/midway-reduce10.jpg" style="width:100%">
      </div>
      <div class="column">
        <img src="images/dinner0-reduce10.jpg" style="width:100%">
      </div>
    <div class="column">
    <img src="images/dinner1-reduce10.jpg" style="width:100%">
      </div>
    </div>
    '''

def tablerow(link, name, description):
    return '<tr><td><a href="%(link)s">%(name)s</td><td>%(description)s</td></tr>' % \
        {'link':link, 'name':name, 'description':description}


def section(name):
    pass

def toc():
    return r'''
    <a id="top"></a>
    <ul>
      <li><a href="#tutorials">Tutorials</a></li>
      <li><a href="#wanna-feed-your-brain">Wanna feed your brain?</a></li>      
      <li><a href="#courses">Courses</a></li>      
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

def head():
    return r'''
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

def webpage():
    return r'''
<html>
  
  %(head)s
  
  <body style="font-family: arial">

    %(header)s
    
    <hr>
    %(toc)s
    
    <hr>
    %(courses)s
    %(tutorials)s
    %(wanna_feed_your_brain)s
  
  </body>
</html>
    ''' % \
        {'head':head(),
         'header':header(),
         'toc':toc(),
         'tutorials':tutorials(),
         'wanna_feed_your_brain':wanna_feed_your_brain(),
         'courses':courses()}

def courses():
    return r'''<h2><a id="courses">Courses</a> <a href="#top" style="font-size:16px">top</a></h2>
    In the future all my notes will be public. Right now they are all under heavy construction.
    <ul>
    <a href="http://ciss145.pythonanywhere.com">CISS145 (Python)</a>
    <a href="http://ciss170.pythonanywhere.com">CISS170 (Intro CIS)</a>
    <a href="http://ciss176.pythonanywhere.com">CISS176 (Intro CS)</a>
    <a href="http://ciss234.pythonanywhere.com">CISS234 (VB)</a>
    <a href="http://ciss238.pythonanywhere.com">CISS238 (Java)</a>
    <a href="http://ciss240.pythonanywhere.com">CISS240 (Intro Prog)</a> 
    <a href="http://ciss245.pythonanywhere.com">CISS245 (Adv Prog)</a> 
    <a href="http://ciss312.pythonanywhere.com">CISS312 (ACM)</a>
    <a href="http://ciss350.pythonanywhere.com">CISS350 (Alg-1)</a>
    <a href="http://ciss358.pythonanywhere.com">CISS358 (Alg-2)</a>
    <a href="http://ciss360.pythonanywhere.com">CISS360 (Assembly)</a>
    <a href="http://ciss362.pythonanywhere.com">CISS362 (Automata)</a>
    <a href="http://ciss375.pythonanywhere.com">CISS375 (Compilers)</a>
    <a href="http://ciss380.pythonanywhere.com">CISS380 (Graphics)</a>
    <a href="http://ciss410.pythonanywhere.com">CISS410 (Ntwks)</a>
    <a href="http://ciss430.pythonanywhere.com">CISS430 (DB)</a>
    <a href="http://ciss438.pythonanywhere.com">CISS438 (OOAD)</a>
    <a href="http://ciss445.pythonanywhere.com">CISS445 (PL)</a>
    <a href="http://ciss450.pythonanywhere.com">CISS450 (AI)</a>
    <a href="http://ciss451.pythonanywhere.com">CISS451 (Crypto)</a>
    <a href="http://ciss465.pythonanywhere.com">CISS465 (SE)</a>
    <a href="http://ciss494.pythonanywhere.com">CISS493/4 (Senior sem)</a>
    <a href="http://math325.pythonanywhere.com">MATH325 (DM 2)</a>
    <a href="http://ciss999.pythonanywhere.com">Computer vision</a>
    <a href="http://ciss998.pythonanywhere.com">Qt</a>
    </ul>


if __name__ == '__main__':
    print(webpage())
