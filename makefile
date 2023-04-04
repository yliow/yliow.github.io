run:
	-mkdir xemacs/ 
	-mkdir vmware/ 
	cp ../xemacs/main.pdf xemacs/main.pdf
	cp ../vmware/vmwareplayer.pdf vmware/vmwareplayer.pdf
	git add .; git commit -m"no msg"; git push
	xdg-open index.html
	firefox https://yliow.github.io/index.html &

