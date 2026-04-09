# Coin Flip Simulator

A modular coin flip simulator with configurable bias, statistical summary output, and a result chart.

## Features

- Simulates any number of flips
- Optional weighted probability for heads (`0.0` to `1.0`)
- Outputs count totals and probabilities for each outcome
- Calculates longest streak in the sequence
- Visualizes results using a bar chart

## Project Structure

- `main.py` - input flow and result display
- `simulation.py` - coin flip simulation logic
- `stats.py` - probability and streak calculations
- `visualization.py` - plotting utilities

## Concepts Practiced

- Modular Python design across multiple files
- Input validation and numeric constraints
- Statistical post-processing on simulation output
- Basic data visualization with `matplotlib`

## Requirements

Install dependencies from the repository root:

```bash
pip install -r coin_flip_sim/requirements.txt
```

## Run

From the repository root:

```bash
python coin_flip_sim/main.py
```
