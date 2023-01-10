run:
	-mkdir xemacs/ 
	cp ../xemacs/main.pdf xemacs/main.pdf
	git add .; git commit -m"no msg"; git push
	firefox https://yliow.github.io/index.html &

