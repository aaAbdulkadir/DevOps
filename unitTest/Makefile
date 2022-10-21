virtual:
	pip install virtualenv &&\
	python3 -m venv venv
install:
	pip install --upgrade pip &&\
	pip install -r requirements.txt
test:
	python test.py
black:

format:
	black *.py
lint:
	python --disable=R,C *.py
all: virtual install test black format lint