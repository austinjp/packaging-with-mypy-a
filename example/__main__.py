import ujson
from packaging_with_mypy_b import sub_package

sub_package.gunicorn # Does nothing, but will cause mypy to barf if there are issues.

out: str = ujson.dumps({"Hello":"world!"})

print(out)
