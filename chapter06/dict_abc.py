from collections.abc import Mapping, MutableMapping

# dict 属于mapping
a = {}

print(isinstance(a, MutableMapping))
