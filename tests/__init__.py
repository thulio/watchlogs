import sys

if sys.version_info >= (3, 4):
    # mock is part of python3 stdlib
    from unittest import mock
    sys.modules['mock'] = mock
