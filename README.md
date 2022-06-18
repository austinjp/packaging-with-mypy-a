# packaging-with-mypy-a

Set up virtual environment and install dependencies:

```
python3.9 -m venv venv
source venv/bin/activate
pip install -U pip
pip install -r requirements.txt
```

Generate stubs for example code, plus a package which does not have stubs available via Typeshed:

```
stubgen -o ./stubs ./example
stubgen -o ./stubs -m packaging_with_mypy_b
```

Unfortuantely, `stubgen` fails to create `stubs/packaging_with_mypy_b/sub_package/__init__.pyi`, so create that file. Since `packaging_with_mypy_b.sub_package` imports `gunicorn`, create the file with the following contents:

```
import gunicorn as gunicorn
```

Generate stubs for further packages that are imported by `packaging_with_mypy_b`, i.e. `gunicorn`:

```
stubgen -o ./stubs -m gunicorn
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
