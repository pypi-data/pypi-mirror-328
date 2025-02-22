# perchance-dsl

Ever read Python if-elif-else blocks and thought, hmm too simple? perchance-dsl is a Python-based domain-specific language (DSL) that provides a more readable syntax for conditional statements, replacing traditional `if-elif-else` blocks.

## Features
- Replace `if` statements with `perchance`
- Replace `elif` statements with `or perchance`
- Replace `else` statements with `certainly`
- Execute `.pyp` scripts directly using the `perchance` command

## Installation

Install Perchance DSL via pip:

```bash
pip install perchance-dsl
```

## Usage

### **Writing a `.pyp` Script**
Create a file, e.g., `example.pyp`, and write:

```python
x = 5

perchance x > 0:
    print("x is positive")
or perchance x == 0:
    print("x is zero")
certainly:
    print("x is negative")
```

### **Running a `.pyp` Script**
Run the script using:

```bash
perchance example.pyp
```

## Contributing
Feel free to open issues or contribute via pull requests on [GitHub](https://github.com/ehrev/perchance-dsl).

## License
This project is licensed under the MIT License.
