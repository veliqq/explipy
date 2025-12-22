import traceback
import sys
from explipy.parser import parse_traceback

def test_parse_traceback():
    try:
        x = 1 / 0
    except ZeroDivisionError:
        exc_type, exc_value, exc_tb = sys.exc_info()
        frames = parse_traceback(exc_tb)
        assert isinstance(frames, list)
        assert len(frames) > 0
        assert "code_line" in frames[0]
