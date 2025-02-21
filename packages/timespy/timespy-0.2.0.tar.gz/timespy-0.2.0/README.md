# TimeSpy ⏱
Timespy is a lightweight Python decorator that measures the execution time of functions, providing an easy way to analyze and optimize performance.

## Installation
```sh
pip install timespy
```

## Usage

```sh
from timespy import timer

@timer
def my_function():
    import time
    time.sleep(1)

my_function()
print(f"Execution time: {my_function.exec_time:.6f}s")
```

## License

TimeSpy is licensed under the GNU General Public License v3 (GPLv3).
See LICENSE for more details.