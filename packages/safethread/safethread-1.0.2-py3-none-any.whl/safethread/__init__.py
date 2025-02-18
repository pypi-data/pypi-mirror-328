# safethread/__init__.py

"""
The `safethread` package provides a collection of thread-safe utilities for managing data structures and synchronization in multi-threaded environments.

The package is designed to ensure safe, concurrent operations on common Python data structures such as lists, dictionaries among others.

### **Modules:**
- **datatype**: Provides thread-safe data structures like `SafeList` and `SafeDict`.
- **thread**: Provides thread-safe classes for multi-threaded programming like `Subprocess`.
- **utils**: Offers utility functions and classes.

### **Features:**
- **Thread-Safe Data Structures**: Safe implementations of common data structures (list, dict) to avoid race conditions in concurrent threads.
- **Thread Synchronization**: Use of Python's `threading.Lock` to manage concurrent access to shared resources.
- **Utility Functions**: Tools to handle thread management and synchronization, including waiting and timeout utilities.

### **Installation:**
- Install via PyPI: `pip install safethread`
- Clone the repository for local development: `git clone https://github.com/andre-romano/safethread.git`

### **License:**
- Apache-2.0 License
"""
