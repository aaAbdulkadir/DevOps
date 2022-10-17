# Makefile

- In a makefile, it is like docker compse in terms of syntax
- If you run 'make' in the cli, it runs the whole makefile
- If you want to run one part of the makefile, you type make {name} e.g.

```bash
install:
    pip install -r requirements.txt
```

```bash
make install
```
- Makefile is useful for running a whole set of commands in concession

# Testing

- Modules: Pytest, pylint, format with black, ipython

# Virtual Environment

- Creating a virtual environment where I download specifics dependencies so that it is isolated from my machine.

- To create a virtual environment

```bash
    python3 -m venv venv
```

- To get into the virtual environment

```bash
    source venv/bin/activate
```

- To get out of the virtual environment

```bash
    deactivate
```
