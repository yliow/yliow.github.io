run: index.html
	-mkdir pdfs
	-mkdir pdfs/xemacs/ 
	-mkdir pdfs/xemacs-python/ 
	-mkdir pdfs/vmware/
	-mkdir pdfs/unix1-1/
	-mkdir pdfs/unix1-1-python/
	-mkdir pdfs/gpp/
	-mkdir pdfs/make/
	-mkdir pdfs/gdb/
	-mkdir pdfs/memory-debugging/
	-mkdir pdfs/git/
	-mkdir pdfs/googletest/
	-mkdir pdfs/latex/
	-mkdir pdfs/latex-graph/
	-mkdir pdfs/latex-automata/
	-mkdir pdfs/latex-2d/
	-mkdir book/
	-mkdir article/
	cp ../xemacs/main.pdf           pdfs/xemacs/main.pdf
	cp ../xemacs-python/main.pdf    pdfs/xemacs-python/main.pdf
	cp ../vmware/vmwareplayer.pdf 	pdfs/vmware/vmwareplayer.pdf
	cp ../unix1-1/main.pdf       	pdfs/unix1-1/main.pdf
	cp ../unix1-1-python/main.pdf   pdfs/unix1-1-python/main.pdf
	cp ../gpp/main.pdf 	      	pdfs/gpp/main.pdf
	cp ../make/main.pdf 	      	pdfs/make/main.pdf
	cp ../gdb/main.pdf 	      	pdfs/gdb/main.pdf
	cp ../memory-debugging/main.pdf pdfs/memory-debugging/main.pdf
	cp ../git/main.pdf 		pdfs/git/main.pdf
	cp ../googletest/main.pdf 	pdfs/googletest/main.pdf
	cp ../latex/main.pdf 		pdfs/latex/main.pdf
	cp ../latex-graph/main.pdf 	pdfs/latex-graph/main.pdf
	cp ../latex-automata/main.pdf 	pdfs/latex-automata/main.pdf
	cp ../latex-2d/main.pdf 	pdfs/latex-2d/main.pdf
	cp ../latex-templates/book.tar.gz book/book.tar.gz
	cp ../latex-templates/article.tar.gz article/article.tar.gz
	python main.py
	git add .; git commit -m"no msg"; git push
	xdg-open index.html &

index.html: main.py
	python main.py

v:
	firefox index.html &

pics:
	firefox pics.html &
