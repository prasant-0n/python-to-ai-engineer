# Chapter 00.01 — How Python Executes a Program

## Learning Objectives
- [ ] Distinguish Python source code, bytecode, and machine instructions.
- [ ] Explain the roles of a Python implementation and runtime.
- [ ] Identify CPython as the standard, widely used Python implementation.
- [ ] Run a program from a terminal and observe output.
- [ ] Distinguish syntax errors from runtime exceptions.

## Starter Example
Create `hello.py`:

```python
def main() -> None:
    print("Hello, AI Engineer!")


if __name__ == "__main__":
    main()
```

Run it from the repository root:

```bash
python --version
python phases/phase-00-engineering-foundation/chapter-00.01-how-python-executes/hello.py
```

## Investigation Tasks
1. Record the Python version and implementation available.
2. Explain what happens from command invocation to output.
3. Compare a syntax error with a runtime exception.
4. Investigate how CPython compiles code to bytecode and executes it.
5. Explain why "Python is interpreted" is an incomplete description of CPython's execution.

## Exercise
Modify the program to accept a name, print a greeting, handle empty input deliberately, and add a test or documented manual test cases.

## Assessment
1. What is an interpreter?
2. What is CPython?
3. How does bytecode differ from native machine code?
4. What happens when Python encounters invalid syntax?
5. What evidence helps investigate a runtime exception?

## Completion Evidence
Record answers, implementation, and test results in `PROGRESS.md`.
