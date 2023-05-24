import sys

f = open('PublicationsonCCCS.html', 'r'); s = f.read(); f.close()

BEGIN = """<p class="c0 c4"><span class="c1"></span></p><p class="c0"><span class="c1">"""
END = """</span></p>"""

while 1:
    f = open('PublicationsonCCCS.html', 'r'); s = f.read(); f.close()
    i = s.find(BEGIN)
    j = s.find(END, i + len(BEGIN))
    if i == -1 or j == -1: break
    
    print(); print("**** OLD " + 60*"*")
    print(s[i - 30:j + len(END) + 30])
    print(60*"*")

    t = s[:i] + "<p>\n" + s[i + len(BEGIN):j] + "\n</p><br>\n\n" \
        + s[j + len(END):]
    print(); print("**** NEW " + 60*"*")
    print(t[i - 30:j + len(END) - len(BEGIN) + 30])
    print(60*"*")
    print(); print()
    input("enter to continue or Ctrl-C ... ")
    f = open('PublicationsonCCCS.html', 'w'); f.write(t); f.close()
