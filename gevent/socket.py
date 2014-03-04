import sys

if sys.version_info[0] >= 3:
    from gevent import socket3 as _source
else:
    from gevent import socket2 as _source

for key in _source.__dict__:
    if key.startswith('__') and key not in '__implements__ __dns__ __all__ __extensions__ __imports__'.split():
        continue
    globals()[key] = getattr(_source, key)
