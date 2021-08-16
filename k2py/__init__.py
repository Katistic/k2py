from k2py import enum

for attr in dir(enum):
    if not attr.startswith("__"):
        globals()[attr] = getattr(enum, attr)