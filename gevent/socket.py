import sys

if sys.version_info[0] >= 3:
    from gevent import socket3 as _source
else:
    from gevent import socket2 as _source

globals().update(_source.__dict__)
