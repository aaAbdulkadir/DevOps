SHELL=./make_venv.sh
virtual:
	pip install virtualenv &&\
	python3 -m venv venv &&\
	pwd
install:
	pip install --upgrade pip &&\
	pip install -r requirements.txt
test:
	python test.py
format:
	black *.py
lint:
	python --disable=R,C *.py