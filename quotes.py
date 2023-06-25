# Add quotes below. Separate by blank line.
quotes = '''
“What matters isn’t extraordinary ability but extraordinary effort.”

“Sometimes it is the people no one can imagine anything of who do the things no one can imagine.”

“It is not that I'm so smart. But I stay with the questions much longer.”

“If you can't explain it simply, you don't understand it well enough.”

“What the imagination seizes as beauty must be truth.”

“Life stands before me like an eternal spring with new and brilliant clothes.”

“He who loves practice without theory is like the sailor who boards ship without a rudder and compass and never knows where he may cast.”

"This is a test."
'''

quotes = quotes.split('\n')
quotes = [x.strip() for x in quotes if x.strip() != '']

def index():
    quotes_html = ''
    for q in quotes:
        quotes_html = quotes_html + ('<p>%s</p><br>' % q)

    return r'''

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

<h2>Quotes</h2>

    <table style="border-collapse:collapse; border : 1px solid white;">
    
    <tr>
    <td>''' + \
        quotes_html + \
    '''<td width="10%%">
    <div class="detailImgWrapper"><img src="images/image1.png" width="200"/></div>
    <div class="detailImgWrapper"><img src="images/image3.png" width="200"/></div>
    <div class="detailImgWrapper"><img src="images/image5.png" width="200"/></div>
    </td>
    </tr>
    </table>
    ''' 
