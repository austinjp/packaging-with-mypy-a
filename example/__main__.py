import ujson
from packaging_with_mypy_b import sub_package

# The next two lines will cause mypy to complain if there are problems.
import gunicorn
sub_package.gunicorn

# Hello, world!
out: str = ujson.dumps({"Hello":"world!"})
print(out)
