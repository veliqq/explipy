from .utils import extract_exception_name

def get_explanation_for(exc_type, exc_value, frames):

    name = extract_exception_name(exc_type)
    msg = str(exc_value)

    # --- Python Built-ins ---
    if "ArithmeticError" in name:
        return "A generic arithmetic problem occurred (subclasses include OverflowError, ZeroDivisionError, FloatingPointError)."
    if "FloatingPointError" in name:
        return "A floating-point calculation produced an error."
    if "OverflowError" in name:
        return "A numeric operation exceeded the maximum representable value."
    if "ZeroDivisionError" in name:
        return "You attempted to divide by zero, which is not allowed."
    if "RecursionError" in name:
        return "Your program recursed too deeply and hit the recursion limit."

    if "EOFError" in name:
        return "End-of-file reached unexpectedly while reading input."
    if "KeyboardInterrupt" in name:
        return "The program was interrupted by the user (Ctrl+C)."
    if "MemoryError" in name:
        return "Your program ran out of memory."
    if "SystemExit" in name:
        return "The program was asked to exit via sys.exit()."

    if "TypeError" in name:
        return f"You used a value of the wrong type: {msg}"
    if "AttributeError" in name:
        if "NoneType" in msg:
            return "You tried to access an attribute or method on a variable that is None."
        return f"An expected attribute or method was missing: {msg}"
    if "NameError" in name:
        return f"A variable was used before being defined: {msg}"
    if "UnboundLocalError" in name:
        return f"A local variable was referenced before assignment: {msg}"
    if "AssertionError" in name:
        return f"An assert statement failed: {msg}"

    if "IndexError" in name:
        return "You tried to access a list or tuple index that is out of range."
    if "KeyError" in name:
        key = msg.strip("'\"")
        return f"You tried to access the key '{key}' in a dictionary, but it does not exist."
    if "StopIteration" in name:
        return "An iterator ran out of items."

    if "OSError" in name:
        return f"A system-related error occurred: {msg}"
    if "FileNotFoundError" in name:
        return f"The file specified could not be found: {msg}"
    if "PermissionError" in name:
        return f"Permission denied when trying to access a file or resource: {msg}"
    if "BlockingIOError" in name:
        return f"An I/O operation would block and cannot proceed: {msg}"

    if "ImportError" in name or "ModuleNotFoundError" in name:
        return f"A required module could not be imported: {msg}"

    if "ValueError" in name:
        return f"A value is incorrect or invalid: {msg}"
    if "UnicodeError" in name or "UnicodeEncodeError" in name or "UnicodeDecodeError" in name:
        return f"A unicode encoding/decoding error occurred: {msg}"

    if "NotImplementedError" in name:
        return "This feature or method is not implemented yet."
    if "RuntimeError" in name:
        return f"A runtime error occurred: {msg}"
    if "SystemError" in name:
        return f"A low-level system error occurred: {msg}"
    if "ReferenceError" in name:
        return f"A weak reference accessed an object that no longer exists: {msg}"
    if "StopAsyncIteration" in name:
        return "An asynchronous iterator ran out of items."

    # --- NumPy Exceptions ---
    if "numpy" in name.lower():
        if "IndexError" in name or "out of bounds" in msg:
            return "NumPy array index is out of bounds."
        if "ValueError" in name or "could not broadcast" in msg:
            return "NumPy arrays have incompatible shapes or values."
        if "TypeError" in name:
            return "NumPy operation used the wrong data type."
        return f"A NumPy error occurred: {msg}"

    # --- Pandas Exceptions ---
    if "pandas" in name.lower():
        if "KeyError" in name:
            return "You tried to access a non-existent column or index in a DataFrame/Series."
        if "ValueError" in name:
            return "A Pandas operation received an invalid value (e.g., wrong length)."
        if "IndexingError" in name:
            return "You attempted an invalid indexing operation on a DataFrame or Series."
        return f"A Pandas error occurred: {msg}"

    # --- Requests Exceptions ---
    if "requests" in name.lower():
        if "ConnectionError" in name:
            return "Requests failed to connect to the server."
        if "Timeout" in name:
            return "The HTTP request timed out."
        if "HTTPError" in name:
            return f"HTTP request returned an error response: {msg}"
        return f"A Requests library error occurred: {msg}"

    # --- Fallback ---
    return f"No specific explanation available for {name}. Check the traceback for details."
