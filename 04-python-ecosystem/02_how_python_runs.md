# How a Python program runs

1. The tokenizer cuts source into tokens
2. The parser builds an abstract syntax tree
3. The compiler emits bytecode
4. The evaluator runs bytecode on a stack machine

Memory: every object has a reference count. When it hits zero, the object is freed. Cycles (A points to B points to A) are collected by the generational garbage collector.

Threads: CPython's GIL means one thread runs Python bytecode at a time. **I/O-bound** work still benefits from threads. **CPU-bound** work needs `multiprocessing`, vectorized NumPy, or a free-threaded build of Python 3.13+.

For this lab: vectorize with NumPy before you reach for threads.
