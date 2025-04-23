#===========================================================================
# SMALLEST HTML FRAGMENTS
#===========================================================================
def cctt():
    return r'''<a href="http://cctt0.pythonanywhere.com/">Royal Ping Pong Club</a>'''
def work_study():
    return r'''Work study:
    <a href="https://docs.google.com/document/d/1uPx4N4WrRhDfcajIs7PwcfdV9Q4fBqpqZwvsogfAn5w/edit?usp=drive_link">page</a> | 
    <a href="https://drive.google.com/drive/folders/0BzjYrK0VFuMWbjFDTnhsUzhHQkE?resourcekey=0-0HJH3q7E1lDQ_9IHyd6olg&usp=drive_link">folder</a>'''
def cs101():
    return r'''<a href='https://docs.google.com/presentation/d/1v_YISntWpguP-t-SwrhjT1537UwmgybZe5mGzwP_11w/edit?usp=sharing'>CS101 Guide to CCCS (HHGTT CCCS)</a> |
    <a href='https://docs.google.com/spreadsheets/d/1km1oFGXvq5QSBqlOPGtfQCmo7F_tl9-dX6H_RuTJ4KM/edit?usp=sharing'>course rotation</a>
    |
    <a href='http://catalog.ccis.edu/content.php?catoid=28&navoid=3576#ciss'>course rotation at ccis.edu</a>
    '''

def grad_school_q_and_a():
    return r'''<a href='https://docs.google.com/document/d/1eAzjxhdGNL15Bar-NsuEWVvCkTteMwa6MPJqNHICgVw/edit'>Grad school Q&A</a>'''

#def publication_about_cccs():
#    return r'''<a href='google-drive-downloads/PublicationsonCCCS.html'>Publications about CCCS</a>'''

def reu():
    return r'''
    REU (Research Experiences for Undergraduates - a nationwide NSF funded summer search program)
    <ul>
    <li>Andrew Woods. 
    <li>Michael Fisher.
    <li>Eric Garcis. 2024. REU at University of Missouri at Columbia. 
    "Hardware trojan detection via In-context Learning of Large Language Models"
    (Advisors: Dr. Khaza Anuarul Hoque, Dr. Prasad Calyam; 
    Graduate Student Mentors: Ripan Kumar Kundu; 
    Research Students: Eric Garcia, Ethan Grassia)
    <li>Robert Oladayo Oyedeji. 2025. REU at University of Missouri at Columbia.
    <li>Cole Schwandt. 2025. REU at Missouri University of Science and Technology.
    </ul>
    '''
    
def publication_about_cccs():
    return r'''<a href='google-drive-downloads/PublicationsonCCCS.html'>Publications about CCCS</a>'''

def companies():
    return r'''<a href='pdfs/companies/main.pdf'>Companies that hire my graduates</a> | or <a href='https://docs.google.com/document/d/1SPCaGycXVdnCXX5L-b2FzQ01kXcIjCkNOE8TyEj_PC4/edit?usp=sharing'>here</a>'''

def cs_hangout():
    return r'''<a href ='http://bit.ly/cc_cs_hangout'>CS Hangout</a>. BRN = Brown Hall.
    <ul>
    <li><font color='red'>For finals week cram ... </font>
    <ul>
    <li>Fri 4/18, 4:30PM-10PM, Brown 101
    <li>Mon 4/21, 4:30PM-10PM, Brown 100 & 101
    <li>Tue 4/22, 3PM-10PM, Brown 100 & 101
    <li>Wed 4/23, 4:30PM-10PM, Brown 100 & 101
    <li>Thu 4/24, 3PM-10PM, Brown 100 & 101
    <li>Fri, 4/25, 4:30PM-10PM, Brown 100 & 101
    </ul>
    <li>MWF 4:30PM-6:30PM, BRN-100
    <li>TuTh 3PM-5PM, BRN-100
    </ul>
    '''
def ciss145():
    return r'<a href="http://ciss145.pythonanywhere.com">CISS145 (Python)</a>'

def research():
    return r'''<a href='urics.html'>Research</a> | %s''' % grad_school_q_and_a() 

def quotes():
    return r'<a href="https://docs.google.com/document/d/1i4HYMQqOo0yP3XPTdtZqws2SgaJ71n2ikBd68c8FYig/edit">Quotes</a>'

def classes_for_current_semester():
    return r'''
My classes:
<ul>
 <li> %s
 <li>ciss430 MWF 9:05AM-10:00AM BUH104
 <li>ciss438 MWF 10:10AM-11:05AM BUH104
 <li>ciss350 MWF 11:15AM-12:10PM BUH100 
 <li>ciss240 MWF 01:25PM-02:20PM and Tue 02:00PM-02:55PM BUH104
 <li>ciss245 MWF 02:30PM-03:25PM and Thu 02:00PM-02:55PM BUH104
 <li>ciss451 MWF 3:35PM-4:30PM BUH100 
</ul>
''' % alex()

def pictures_and_videos():
    return r"<a href='https://docs.google.com/document/d/1uGC6ZMQ6OMY8voiTKsuaRYOW2fUQZDdj1QoA-euKGtg/edit?usp=sharing'>Pictures and videos</a>"

def cs_day():
    return r"<a href='cs_day.html'>CS Day</a>"

def cs_jam():
    return r"<a href='https://docs.google.com/document/d/1NGH0XFmeaIfdWVxBzlBK-ehKvilg61Rs9gww6j1FjsQ/edit'>CS.js (CS Jam)</a>"

def department_welcome_lunch():
    return r"<a href='http://bit.ly/cccslunch'>Department welcome lunch</a>"

def end_of_semester_presentations():
    return r"End of semester presentations: <a href='how_to_give_a_talk.html'>How to give a talk</a>"

def end_of_semester_celebration():
    return r"End of semester celebration"

def facebook():
    return r"Facebook"

def cs_club():
    return r"""<a href="https://docs.google.com/document/d/1N3mPEOMjcKJQLtjWQ_-qsvVcVNrDFDdwsB35SPqcxbA/">CS Club</a> | <a href="https://docs.google.com/document/d/1R_7pFL_HV9hSLtdgGbi58uAm71c5d2-Fm9TnV7_sZas/edit#">CS Club meetings</a> (all members are invited)"""

def game_tournaments():
    return r"""<a href="https://docs.google.com/document/d/1roomf0yhSgpk-jC1tw8maa5MfKlnDjlAPSRgLhR6Gck/edit#">Game Tournaments</a>"""

def industrial_connection():
    return r"""<a href="https://docs.google.com/document/d/1SfhwTUO0HX3b6imjGNou_Vjg0uw2gGy1cSLm38w9p64/edit#">Industrial connection</a>"""

def kickoff():
    return r"""Kickoff | <a href="https://docs.google.com/document/d/1QNu_Zt0RhNLgDziYJ779yav-9l9bXuRfckVxglZeM_s/edit?usp=sharing">Committee</a>"""

def media_committee():
    return r"<a href='https://docs.google.com/document/d/1wY-P6JPTw0zQfbonmlYLWbc0nyFErPSzXSE_sX5EY8o/edit?usp=sharing'>Media committee</a>"

def movie_night():
    return r"""<a href="https://docs.google.com/document/d/1rJqBMNCTFRQ2JNAQBfXwWUYXDwjbsml3vIdWP-YQTpI/edit?usp=sharing">Movie night</a>"""

def monday_programming_challenges():
    return r"<a href='https://docs.google.com/document/d/1P-wEe4xqaP7SUwY0QXE8hd2Q0ti_vJb6E5xHRrWZfys/edit?usp=sharing'>Monday Programming Challenges</a>"

def robotics_group():
    return r"<a href='https://docs.google.com/document/d/1z-Mu7qCrj62TJYtnN-FJYYXVqYmGRPSpIcz5eJCt-x4/edit#'>Robotics group</a>"
    
def t_shirt():
    return r"""<a href="https://docs.google.com/document/d/16f147t6G8pnBvP9hGhbVwsK56hLoLaK_S9x5tT8X0vs/edit?usp=sharing">T-shirt</a>
    |
    <a href="https://docs.google.com/document/d/1C32m45nlAsTkeCpOWtrVsI4tK7fKD9tWe1UTZUTjaEM/edit#">Committee</a>"""

def programming_contest():
    return r"""<a href="https://docs.google.com/document/d/1wc3Wov4B4qistaV8csbUm0NyUOn0XbwDEY4BWM5dSoE/edit?usp=sharing">Programming contest</a>
    |
    <a href="https://docs.google.com/document/d/1x_37FDFysT159iKrgJKUosgI6EElMzu9WfDd4b8nokY/edit?usp=sharing">Committee</a>"""

def high_school_programming_contest():
    return '''<a href='https://docs.google.com/document/d/1gjkRumx_jq9VGyxdjBZU9IICerqZr_8wKHaq7nls64Q/edit'> HS Programming contest</a>
    |
    <a href='https://docs.google.com/document/d/1evtUsB7LE-sTPoY5g2BUrptodSErx-Mxks0z3sTrWqM/edit#'>Committee</a>'''

def academic_calendar():
    return r'<a href="pdfs/academic-calendar.pdf">Academic calendar</a>'

def final_exam():
    return r'<a href="pdfs/final-exam.pdf">Final exam</a>'

def academic_calendar_final_exam():
    return academic_calendar() + " | " + final_exam() 

def calendar():
    return r""" Calendar: <a href="https://www.google.com/calendar/embed?src=cc.cs.photos.videos%40gmail.com&ctz=America/Chicago&mode=week">Week</a> | <a href="https://www.google.com/calendar/embed?src=cc.cs.photos.videos%40gmail.com&ctz=America/Chicago&mode=month">Month</a> """

def cccs_google_group():
    return r"""<a href="https://groups.google.com/g/cc_cs/">CCCS google group</a>"""

def cccs_discord():
    return r"""<a href="https://discord.gg/UDCX6wF">CCCS discord</a>
    (
    <a href="https://discordapp.com/download">discord app</a> |
    <a href="cccsdiscord.html">history</a>
    )
    <ul>
    <li>Once you are in, go to “welcome-and-rules”.
    <li>Ask questions in the rooms/channels.
    <li>Right-click on user to send a direct/private msg.
    </ul>
    """

def alex():
    return r"""alex (for work submission):
    <a href='https://yliowsubmit.pythonanywhere.com/ul'>https://yliowsubmit.pythonanywhere.com/ul</a>
    """

def administrative_stuff():
    return r"""
Administrative stuff:
<ul>
<li>Forms: <a href="pdfs/Course_Audit_Form_1.pdf">course audit form</a>
    | <a href="https://drive.google.com/file/d/1YOaFo5nM9X8EHanqufFKAEq_7miwNLvC/view?usp=sharing">prerequisite waiver form</a>
    | <a href="https://drive.google.com/file/d/1qdu3EVnCXhxvEpl3lI_RPYFYqN_O1flu/view?usp=sharing">course withdrawal form</a>
<li>Howto: <a href="https://docs.google.com/document/d/1n4mIGWJWRFDNyDrQstJ64z1ND4zSw89jca0VWp8YbrA/edit?usp=sharing">register for classes</a>
    | <a href="https://docs.google.com/document/d/1Z5Aq_AuCzT6XFSI7OGy6_rEQ7tAJLjvtrJBdcqimAGM/edit?usp=sharing">add a minor</a>
</ul>
    """
