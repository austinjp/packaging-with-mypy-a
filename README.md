# packaging-with-mypy-a

This Python package is to remind me how to build and distributes packages that contain type stubs built with the `stubgen` tool from [`mypy`](https://github.com/python/mypy).

See <https://github.com/austinjp/packaging-with-mypy-b>.

<hr />

## What to do?

Set up virtual environment and install dependencies:

```bash
python3.9 -m venv venv
source venv/bin/activate
pip install -U pip
pip install -r requirements.txt
```

Generate stubs for example code:

```bash
stubgen -o ./stubs ./example
```

Ensure `mypy` knows where all stubs will be found:

```bash
# Where *this* project's stubs will live:
export MYPYPATH=./stubs

# Detect any *.pyi files in packages that bundle them:
export MYPYPATH="${MYPYPATH}":./venv/lib/python3.9/site-packages/

# If using "pip install -e ...", we need to add the
# appropriate dirs in the virtual environment:
export MYPYPATH="${MYPYPATH}":./venv/src/packaging-with-mypy-b/
```

Run `mypy`, static type checks:

```bash
mypy ./example
```

Expected output:

```text
Success: no issues found in 1 source file
```
