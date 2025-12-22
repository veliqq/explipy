# ExpliPy

**Human-readable Python exception explanations.**  
ExpliPy explains Python exceptions in plain English, including NumPy, Pandas, and requests errors. Works automatically for uncaught exceptions with a drop-in hook.

---

## 🚀 Features

- Explain Python built-ins and common library exceptions
- Supports NumPy, Pandas, Requests
- Drop-in `sys.excepthook`** for uncaught exceptions
- Human-readable, beginner-friendly messages
- Safe for production use
- Lightweight, pure Python (no AI required)

---

## 📦 Installation

```bash
pip install explipy
````

---

## 💡 Basic Usage

```python
from explipy import explain_exception

try:
    x = 1 / 0
except Exception:
    explain_exception()
```

**Output:**

```
=== ExpliPy Exception Explainer ===
Type: ZeroDivisionError
Message: division by zero
Explanation: You attempted to divide by zero, which is not allowed.
=================================
```

---

## ⚡ Using the Global Hook

Automatically explain **all uncaught exceptions**:

```python
import explipy

# Install hook globally
explipy.install_hook()

# Example
def divide(a, b):
    return a / b

divide(5, 0)  # ExpliPy will explain automatically
```

---

## 🧪 Library Exceptions Supported

* **Python built-ins**: ZeroDivisionError, KeyError, IndexError, ValueError, AttributeError, etc.
* **NumPy**: array index out-of-bounds, type errors, broadcasting issues
* **Pandas**: missing columns, indexing errors, invalid values
* **Requests**: connection errors, timeouts, HTTP errors

---

## 🔧 Development

```bash
git clone https://github.com/veliqq/explipy.git
cd explipy
pip install -e .[dev]

# Run tests
pytest
```

---

## 📄 License

MIT License

