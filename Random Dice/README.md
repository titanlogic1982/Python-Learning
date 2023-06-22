# Dice Roll Simulator

This Python script uses the numpy and matplotlib libraries to simulate rolling a six-sided die multiple times, and to plot the results of those rolls.

## Description

The script contains two main functions:

1. `roll_die(num_rolls)`: This function uses the numpy function `np.random.randint` to generate an array of random integers between 1 and 6 (inclusive). The `num_rolls` argument determines the size of the array, which simulates the number of times the die is rolled.

2. `main()`: This function calls `roll_die` to simulate rolling a die 100 times. The results are then plotted using matplotlib, with the roll number on the X-axis and the result of the roll on the Y-axis.

## Explanation

```python
import numpy as np
import matplotlib.pyplot as plt
```
These lines import the numpy and matplotlib libraries.

```python
def roll_die(num_rolls):
    return np.random.randint(1, 7, size=num_rolls)
```
This function simulates rolling a die by generating an array of random integers.

```python
def main():
    num_rolls = 100
    rolls = roll_die(num_rolls)
```
The `main()` function sets the number of rolls to 100 and calls the `roll_die()` function to generate the results.

```python
    x = np.arange(1, num_rolls + 1)
    y = rolls
```
Two arrays are created: `x` contains the roll numbers, and `y` contains the results of the rolls.

```python
    plt.plot(x, y, marker='o', linestyle='-', color='blue')
    plt.xlabel('Roll Number')
    plt.ylabel('Die Result')
    plt.title('Results of Die Rolls')
    plt.show()
```
These lines plot the results and display the plot. Each roll is represented by a point on the plot, with the roll number on the X-axis and the result on the Y-axis.

```python
if __name__ == "__main__":
    main()
```
The `main()` function is called if the script is being run directly, allowing the script to be imported as a module in another script without automatically running the `main()` function.
