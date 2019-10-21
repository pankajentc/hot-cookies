init:
	python3.6 -m pip install -r requirements.txt --user
test:
	nosetests -verbosity=2 tests/
