all:
	@cat Makefile

meijutt:
	python3 ./example/meijutt/main.py

install:
	@echo I think nothing special is needed.. If anything, use \'pip3 install xxx\' to install it.

clean:
	rm -rf ./run_log

fast-push:
	git add * &
	git status 
	git commit -m 'updated'
	git push origin master
