# Makefile

- In a makefile, it is like docker compse in terms of syntax
- If you run 'make' in the cli, it runs the whole makefile
- If you want to run one part of the makefile, you type make {thenameyoudeclared} i.e. make run where run is run:
    - e.g. install:
	            pip install -r requirements.txt
    - make install
- Makefile is useful for running a whole set of commands in concession

# Testing

- Modules: Pytest, pylint, format with black, ipython