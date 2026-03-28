pdf:
	#python main.py
	pdflatex --shell-escape Riley-Salladay.tex
	xdg-open Riley-Salladay.pdf
view:
	xdg-open Riley-Salladay.pdf
v:
	xdg-open Riley-Salladay.pdf
cleantmp:
	-rm -rf *.out *.log *.idx *.aux *.pytxcode '__pycache__' 'auto' 'desktop.ini' 'main.py.err' \
	'abc.output' 'texput.log' 'shEsc.tmp' \
	'*.log' '*.aux' '*.out' '*.toc' '*.out' '*.idx' '*.ilg' 'main.vrb' 'main.snm' 'main.nav' \
	'main.py.err' 'main.py.out' 'latex.py' 'main.pytxcode' \
	'makefile.old' 'missfont.log' 'traceback.txt'
c:
	make cleantmp
