from pyutil import *

head = r'''
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>LCARS-X // CCCS TERMINAL COLUMBIA COLLEGE COMPUTER SCIENCE</title>
    <style>
        :root {
            --bg-color: #050811;
            --panel-bg: rgba(10, 25, 50, 0.5);
            --neon-blue: #00f3ff;
            --neon-green: #39ff14;
            --neon-amber: #ffb700;
            --neon-red: #ff3131;
            --border-glow: 0 0 10px rgba(0, 243, 255, 0.3);
            --text-glow: 0 0 8px rgba(0, 243, 255, 0.6);
            --font-family: 'Courier New', Courier, monospace;
        }
        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            cursor: crosshair;
        }
        body {
            background-color: var(--bg-color);
            color: var(--neon-blue);
            font-family: var(--font-family);
            overflow-x: hidden;
            height: 100vh;
            display: grid;
            grid-template-rows: auto 1fr auto;
            background-image: 
                radial-gradient(white, rgba(255,255,255,.2) 2px, transparent 40px),
                radial-gradient(white, rgba(255,255,255,.15) 1px, transparent 30px);
            background-size: 550px 550px, 350px 350px;
            animation: warpDrive 100s linear infinite;
            animation: infimprobDrive 100s linear infinite; /* ?? */
        }
        @keyframes warpDrive {
            from { background-position: 0 0, 40px 60px; }
            to { background-position: 550px 550px, 390px 410px; }
        }
        @keyframes infimprobDrive { /* ?? */
            from { background-position: 0 0, 40px 60px; }
            to { background-position: 550px 550px, 390px 410px; }
        }

        body::before {
            content: " ";
            display: block;
            position: fixed;
            top: 0; left: 0; bottom: 0; right: 0;
            background: linear-gradient(rgba(18, 16, 16, 0) 50%, rgba(0, 0, 0, 0.25) 50%);
            z-index: 9999;
            background-size: 100% 4px;
            pointer-events: none;
        }
        header {
            border-bottom: 2px solid var(--neon-blue);
            padding: 15px 30px;
            background: var(--panel-bg);
            box-shadow: var(--border-glow);
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        .ship-title h1 {
            font-size: 1.8rem;
            letter-spacing: 4px;
            text-shadow: var(--text-glow);
        }
        .ship-status {
            display: flex;
            gap: 20px;
            font-size: 0.8rem;
        }
        .status-node {
            padding: 5px 10px;
            border: 1px solid var(--neon-green);
            color: var(--neon-green);
            border-radius: 4px;
        }
        .main-bridge {
            display: grid;
            grid-template-columns: 250px 1fr 300px;
            gap: 20px;
            padding: 20px;
            height: calc(100vh - 140px);
            overflow: hidden;
        }
        .hud-panel {
            background: var(--panel-bg);
            border: 1px solid var(--neon-blue);
            box-shadow: var(--border-glow);
            border-radius: 8px;
            padding: 20px;
            display: flex;
            flex-direction: column;
            overflow-y: auto;
        }
        .nav-deck { gap: 15px; }
        .nav-btn {
            background: transparent;
            border: 1px solid var(--neon-blue);
            color: var(--neon-blue);
            padding: 12px;
            text-align: left;
            text-decoration: none;
            text-transform: uppercase;
            font-weight: bold;
            font-family: var(--font-family);
            transition: all 0.3s ease;
        }
        .nav-btn:hover, .nav-btn.active {
            background: var(--neon-blue);
            color: var(--bg-color);
            box-shadow: 0 0 15px var(--neon-blue);
        }
        .viewscreen { position: relative; }
        .console-content {
            display: none;
        }
        .console-content.active-view {
            display: block;
        }
        h2 {
            color: var(--neon-amber);
            margin-bottom: 20px;
            border-bottom: 1px dashed var(--neon-amber);
            padding-bottom: 5px;
            text-transform: uppercase;
        }
        p { margin-bottom: 15px; line-height: 1.6; }
        .cmd-line { color: var(--neon-green); margin-bottom: 10px; }
        .telemetry-deck h3 {
            font-size: 0.9rem;
            color: var(--neon-amber);
            margin-bottom: 10px;
            text-transform: uppercase;
        }
        .matrix-box {
            font-size: 0.75rem;
            background: rgba(0,0,0,0.4);
            border: 1px solid rgba(0, 243, 255, 0.2);
            padding: 10px;
            height: 150px;
            overflow: hidden;
            margin-bottom: 20px;
            color: var(--neon-green);
        }
        .bar-graph { display: flex; flex-direction: column; gap: 8px; }
        .bar-row { display: flex; align-items: center; justify-content: space-between; font-size: 0.75rem; }
        .bar-bg { width: 120px; height: 10px; background: rgba(255,255,255,0.1); border: 1px solid var(--neon-blue); }
        .bar-fill { height: 100%; background: var(--neon-blue); width: 50%; }
        footer {
            border-top: 1px solid rgba(0, 243, 255, 0.4);
            padding: 10px 30px;
            font-size: 0.75rem;
            display: flex;
            justify-content: space-between;
            background: rgba(5, 8, 17, 0.9);
        }

        /* ADDED */

        a:link {
  color: #00d2ff;
  text-decoration: underline;
  text-underline-offset: 3px;
  transition: color 0.3s ease, text-shadow 0.3s ease;
}
a:visited {
  color: #a177ff;
  text-decoration: underline;
}
a:hover {
  color: #ffffff;
  text-decoration: underline;
  text-shadow: 0 0 5px #00d2ff, 0 0 10px #00d2ff, 0 0 20px #00d2ff;
}
a:active {
  color: #ff007f;
  text-decoration: underline;
}
        /* ADDED */
        @keyframes smooth-blink {
        0% { opacity: 1; }
        50% { opacity: 0; }
        100% { opacity: 1; }
    }

    .fade-blink {
        animation: smooth-blink 10s ease-in-out infinite; 
    }

    </style>
</head>
'''

header = r'''
    <header>
        <div class="ship-title"><h1>CCCS // COLUMBIA COLLEGE COMPUTER SCIENCE</h1></div>
        <div class="ship-status">
            <div class="status-node" id="clock">STARDATE: 2026.000</div>
            <div class="status-node" style="border-color: var(--neon-amber); color: var(--neon-amber);">SYS_LOAD: OPTIMAL</div>
            <div class="status-node">SHIELDS: 100%</div>
        </div>
    </header>
'''


footer = r'''
    <footer>
        <div>COMMS: <span class="fade-blink">ONLINE // SECURE_LINK</span></div>
        <div>DESIGN BY CONTROL_DECK_OS v4.11</div>
    </footer>
'''

script = r'''
    <script>
        function engageDeck(targetDeckId, buttonElement) {
            document.querySelectorAll('.console-content').forEach(p => p.classList.remove('active-view')); // the top line "root..."
            document.getElementById(targetDeckId).classList.add('active-view'); /* the body */
            document.querySelectorAll('.nav-btn').forEach(b => b.classList.remove('active')); /* turn off nav button */
            buttonElement.classList.add('active'); // make button pressed stay bright
        }
        function updateStardate() {
            const now = new Date();
            document.getElementById('clock').innerText = `STARDATE: ${now.getFullYear()}.${Math.floor((now - new Date(now.getFullYear(), 0, 0)) / 86400000)}`;
        }
        setInterval(updateStardate, 60000); updateStardate();
        const box = document.getElementById('matrix-terminal');
        const logs = ["[INFO] Node pinged.",
                      "[WARN] Solar flare radiation.",
                      "[WARN] Vogon ship 3.14" + Math.floor(Math.random() * 100) + " ly.",
                      "[SYS] Route updated.",
                      "[INFO] Port 8080 active.",
                      "[INFO] CS welcome lunch 2027 TBD.",
                      "[INFO] Fall 2027 CS kickoff TBD.",
                      "[INFO] Fall 2027 CS Day TBD.",
                      "[INFO] HSPC #11 3/6/2027."];
        setInterval(() => {
            if (box) {
                box.innerHTML += `<br>${logs[Math.floor(Math.random() * logs.length)]}`;
                box.scrollTop = box.scrollHeight;
            }
            const wb = document.getElementById('warp-bar');
            if (wb) wb.style.width = Math.floor(Math.random() * 20 + 75) + '%';
            const iib = document.getElementById('inf-improb-bar');
            if (iib) iib.style.width = Math.floor(Math.random() * 20 + 55) + '%';
        }, 3500);
    </script>
'''


nav_deck = r'''
        <!-- left nav bar -->
        <nav class="hud-panel nav-deck">
            <h3 style="color: var(--neon-amber); font-size: 0.9rem; margin-bottom: 10px;">SECTOR NAV</h3>
            <button class="nav-btn active" onclick="engageDeck('manifesto', this)">[ ] Manifesto</button> <!-- "active" means turn on -->
            <button class="nav-btn" onclick="engageDeck('events', this)">[ ] Events</button>
            <button class="nav-btn" onclick="engageDeck('academics', this)">[ ] Academics</button>
            <button class="nav-btn" onclick="engageDeck('tutorials', this)">[ ] Tutorials</button>
            <button class="nav-btn" onclick="engageDeck('outreach', this)">[ ] Outreach</button>
            <button class="nav-btn" onclick="engageDeck('research', this)">[ ] Research</button>
            <button class="nav-btn" onclick="engageDeck('about', this)">[ ] About</button>
            <button class="nav-btn" onclick="engageDeck('contact_us', this)">[ ] Contact us</button>
        </nav>
'''

telemetry_deck = r'''
        <aside class="hud-panel telemetry-deck">
            <h3>Matrix Diagnostics</h3>
            <div class="matrix-box" id="matrix-terminal">[SYS] Monitoring telemetry...</div>
            <h3>Core Allocation</h3>
            <div class="bar-graph">
                <div class="bar-row"><span>WARP</span><div class="bar-bg"><div class="bar-fill" id="warp-bar" style="width: 85%;"></div></div></div>
                <div class="bar-row"><span>PROP</span><div class="bar-bg"><div class="bar-fill" id="prop-bar" style="width: 42%;"></div></div></div>
                <div class="bar-row"><span>INF IMPROB</span><div class="bar-bg"><div class="bar-fill" id="inf-improb-bar" style="width: 25%;"></div></div></div>
            </div>
        </aside>
'''


def main_page(id_='research',
              cmd_line=r'root@bridge:~# ls -la /var/research/',
              title='Research',
              active_view=True, # true means show up on load
              paragraphs=[
                  ]
              ):
    if active_view: active_view = r'''active-view'''
    xs = []
    for p in paragraphs:
        xs.append('<p>%s</p>\n' % p)
    b = '\n'.join(xs)

    a = r'''
            <div id="%(id_)s" class="console-content %(active_view)s">
                <div class="cmd-line">%(cmd_line)s</div>
                <h2>%(title)s</h2>

                %(b)s
            </div>
         ''' % {'id_':id_, 'cmd_line':cmd_line, 'title':title, 'active_view':active_view, 'b':b}
    return a

manifesto_page = main_page(id_='manifesto',
                           cmd_line='root@bridge:~# cat welcome_msg.txt',
                           title='Greeting, Traveler.',
                           active_view=True,
                           paragraphs=[readfile('manifesto.html'),
                           ])
research_page = main_page(id_='research',
                          cmd_line='root@bridge:~# ls -la /var/research/',
                          title='Research',
                          active_view=False,
                          paragraphs=[readfile('research.html')])
outreach_page = main_page(id_='outreach',
                          cmd_line='root@bridge:~# ls -la outreach.dat',
                          title='Outreach',
                          active_view=False,
                          paragraphs=[readfile('outreach.html')])
events_page = main_page(id_='events',
                        cmd_line='root@bridge:~# ls -la /var/events.dat',
                        title='Events',
                        active_view=False,
                        paragraphs=[readfile('events.html')])
tutorials_page = main_page(id_='tutorials',
                        cmd_line='root@bridge:~# cat tutorials.dat',
                        title='Tutorials',
                        active_view=False,
                        paragraphs=[readfile('tutorials.html')])
academics_page = main_page(id_='academics',
                        cmd_line='root@bridge:~# cat academics.dat',
                        title='Academics',
                        active_view=False,
                        paragraphs=[readfile('academics.html')])
contact_us_page = main_page(id_='contact_us',
                        cmd_line='root@bridge:~# cat /var/log/contact_us.dat',
                        title='Contact Us',
                        active_view=False,
                        paragraphs=[readfile('contact_us.html')])
about_page = main_page(id_='about',
                       cmd_line='root@bridge:~# cat /var/log/about.dat',
                       title='About CCCS starship #2: SS Systems Horizon',
                       active_view=False,
                       paragraphs=[readfile('about.html')])
classes_page = main_page(id_='classes',
                       cmd_line='root@bridge:~# cat /var/log/classes.dat',
                       title='Academics > Classes',
                       active_view=False,
                       paragraphs=[readfile('classes.html')])
alex_page = main_page(id_='alex',
                       cmd_line='root@bridge:~# cat /var/log/alex.dat',
                       title='Academics > Alex',
                       active_view=False,
                       paragraphs=[readfile('alex.html')])
calendars_page = main_page(id_='calendars',
                       cmd_line='root@bridge:~# cat /var/log/calendars.dat',
                       title='Academics > Calendars',
                       active_view=False,
                       paragraphs=[readfile('calendars.html')])

viewscreen = r'''
     <section class="hud-panel viewscreen">
            %(manifesto_page)s
            %(research_page)s
            %(events_page)s
            %(outreach_page)s
            %(academics_page)s
            %(tutorials_page)s
            %(contact_us_page)s
            %(about_page)s
            %(classes_page)s
            %(alex_page)s
            %(calendars_page)s
        </section>   
''' % {'manifesto_page':manifesto_page,
       'research_page':research_page,
       'outreach_page':outreach_page,
       'events_page':events_page,
       'tutorials_page':tutorials_page,
       'academics_page':academics_page,
       'contact_us_page':contact_us_page,
       'about_page':about_page,
       'classes_page':classes_page,
       'alex_page':alex_page,
       'calendars_page':calendars_page,
       }

s = r'''
<!DOCTYPE html>
<html lang="en">
%(head)s
<body>
    %(header)s
    <main class="main-bridge">
        %(nav_deck)s
        %(viewscreen)s
        %(telemetry_deck)s
    </main>
    %(footer)s
    %(script)s
</body>
</html>
'''


def main():
    t = s % {'head':head,
             'header':header,
             'nav_deck':nav_deck,
             'viewscreen':viewscreen,
             'telemetry_deck':telemetry_deck,
             'footer':footer,
             'script':script,
    }
    writefile('index.html', t)

if __name__ == '__main__':
    main()
