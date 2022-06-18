import ujson
import packaging_with_mypy_b

out: str = ujson.dumps({"Hello":"world!"})

print(out)
