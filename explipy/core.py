import sys
from .parser import parse_traceback
from .rules import get_explanation_for
from .utils import safe_str, truncate_message

def explain_exception(exc_type=None, exc_value=None, tb=None, print_output=True):
    """
    Explain an exception in plain English.
    If called with no arguments, uses sys.exc_info().
    """

    if exc_type is None or exc_value is None or tb is None:
        exc_type, exc_value, tb = sys.exc_info()

    if exc_type is None:
        raise RuntimeError("No exception to explain")

    frames = parse_traceback(tb)
    exc_msg = truncate_message(safe_str(exc_value))
    explanation = get_explanation_for(exc_type, exc_msg, frames)

    if print_output:
        print("=== ExpliPy Exception Explainer ===")
        print(f"Type: {exc_type.__name__}")
        print(f"Message: {exc_msg}")
        print("Explanation:", explanation)
        print("=================================")

    return explanation


def install_hook(print_output=True, exit_after=True):

    def hook(exc_type, exc_value, tb):
        explain_exception(exc_type, exc_value, tb, print_output=print_output)
        if exit_after:
            sys.__excepthook__(exc_type, exc_value, tb)

    sys.excepthook = hook
