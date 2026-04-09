# Calculator

A command-line calculator that evaluates basic arithmetic expressions between two user-provided numbers.

## Features

- Supports addition, subtraction, multiplication, and division
- Re-prompts for invalid operators
- Allows repeated calculations in a loop

## Concepts Practiced

- User input handling
- Conditional validation loops
- Expression evaluation and output formatting

## Run

From the repository root:

```bash
python calculator/calculator.py
```

## Notes

- The current implementation uses `eval()` to compute results.
- This is acceptable for controlled learning input, but production tools should avoid `eval()` for security reasons.
