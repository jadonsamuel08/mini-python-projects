# Password Generator

A command-line password generator that creates secure passwords with configurable character sets and length.

## Features

- Configurable length (minimum enforced)
- Optional inclusion of:
  - Lowercase letters
  - Uppercase letters
  - Digits
  - Symbols
- Ensures at least one character from each selected category
- Uses cryptographically secure randomness (`secrets`)
- Repeat-generation workflow

## Concepts Practiced

- Secure random generation with the `secrets` module
- Input validation and reusable helper functions
- Character pool construction and constraints
- Shuffling and string assembly logic

## Run

From the repository root:

```bash
python password_generator/password_generator.py
```
