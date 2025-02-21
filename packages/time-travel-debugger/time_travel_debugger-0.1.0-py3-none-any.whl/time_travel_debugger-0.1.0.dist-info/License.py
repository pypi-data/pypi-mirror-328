
---

## **🔹 Task 5: Creating Tests**
📌 **`tests/test_debugger.py`**
```python
from time_travel_debugger import TimeTravelDebugger

def test_debugger():
    debugger = TimeTravelDebugger()
    assert debugger.execution_log == []

test_debugger()
