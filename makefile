run: index.html
	-mkdir xemacs/ 
	-mkdir vmware/
	-mkdir unix1-1/
	-mkdir gpp/
	-mkdir make/
	-mkdir gdb/
	-mkdir memory-debugging/
	-mkdir git/
	-mkdir googletest/
	-mkdir latex/
	-mkdir latex-graph/
	-mkdir latex-automata/
	-mkdir latex-2d/
	-mkdir book/
	cp ../xemacs/main.pdf xemacs/main.pdf
	cp ../vmware/vmwareplayer.pdf vmware/vmwareplayer.pdf
	cp ../unix1-1/main.pdf unix1-1/main.pdf
	cp ../gpp/main.pdf gpp/main.pdf
	cp ../make/main.pdf make/main.pdf
	cp ../gdb/main.pdf gdb/main.pdf
	cp ../memory-debugging/main.pdf memory-debugging/main.pdf
	cp ../git/main.pdf git/main.pdf
	cp ../googletest/main.pdf googletest/main.pdf
	cp ../latex/main.pdf latex/main.pdf
	cp ../latex-graph/main.pdf latex-graph/main.pdf
	cp ../latex-automata/main.pdf latex-automata/main.pdf
	cp ../latex-2d/main.pdf latex-2d/main.pdf
	cp ../latex-templates/book.tar.gz book/book.tar.gz
	git add .; git commit -m"no msg"; git push
	xdg-open index.html
	firefox https://yliow.github.io/index.html &

index.html:
	python main.py > index.html
