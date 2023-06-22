import numpy as np
import matplotlib.pyplot as plt

def roll_die(num_rolls):
    # Remove the seed for more randomness
    return np.random.randint(1, 7, size=num_rolls)

def main():
    num_rolls = 100
    rolls = roll_die(num_rolls)

    x = np.arange(1, num_rolls + 1)  # X-axis values
    y = rolls  # Y-axis values

    # Plot the results
    plt.plot(x, y, marker='o', linestyle='-', color='blue')
    plt.xlabel('Roll Number')
    plt.ylabel('Die Result')
    plt.title('Results of Die Rolls')
    plt.show()

if __name__ == "__main__":
    main()