all:
	@cat Makefile
trans:
	python3 ./example/gg_translate/main.py

meijutt:
	python3 ./example/meijutt/main.py
tvshow:
	python3 ./example/tvshow/main.py
install:
	pip3 install IPython
	# @echo I think nothing special is needed.. If anything, use \'pip3 install xxx\' to install it.

clean:
	rm -rf ./run_log

fast-push:
	git add * &
	git status 
	git commit -m 'updated'
	git push origin master
