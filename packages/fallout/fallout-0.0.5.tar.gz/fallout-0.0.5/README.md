# Fallout Library

The Fallout library provides simple methods for calculating decay times, remaining mass, and radiation dose (siverts) for a set of predefined radioactive substances.

## Installation

Install via pip:

```bash
pip install fallout
```

## Usage

```python
from fallout import Fallout

# Create an instance
fallout = Fallout()

# List available substances
substances = fallout.get_radioactive_substances()
print(substances)

# Calculate remaining grams after a number of half-lives
remaining = fallout.calculate_remaining_gram(gram=10, number_of_halflifes=2)
print(remaining)

# Determine risk based on amount of radioactive material
risk, siverts = fallout.calculate_risk("Uranium-235", 5)
print(risk, siverts)
```

## Methods Overview

- `get_radioactive_substances()`: Returns the dictionary of radioisotopes and their properties.
- `calculate_decay_time(type, number_of_halflifes)`: Returns the realistic decay time based on half-lives and isotope data.
- `calculate_remaining_gram(gram, number_of_halflifes)`: Computes how much mass remains after a certain number of half-lives.
- `calculate_siverts(type, gram)`: Calculates the radiation dose in siverts based on mass.
- `calculate_risk(type, gram)`: Gives a risk assessment and dose in siverts.

## Example CLI Usage

If you run the `fallout.py` file directly:
```bash
python fallout.py
```
It will prompt for substance type, amount in grams, and number of half-lives to compute safety and decay information.
