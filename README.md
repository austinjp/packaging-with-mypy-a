# packaging-with-mypy-a

Set up virtual environment and install dependencies:

```
python3.9 -m venv venv
source venv/bin/activate
pip install -U pip
pip install -r requirements.txt
```

Generate stubs for example code:

```
stubgen -o ./stubs ./example
```

Run mypy as a type check:

```
export MYPYPATH=./stubs/
mypy ./example
```

Expected output:

```
Success: no issues found in 1 source file
```
