import random
import matplotlib.pyplot as plt

def simulate_dice_rolls(num_rolls):
    sum_counts = {i: 0 for i in range(2, 13)}
    
    for _ in range(num_rolls):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        roll_sum = dice1 + dice2
        sum_counts[roll_sum] += 1
    
    probabilities = {sum_value: count / num_rolls for sum_value, count in sum_counts.items()}
    
    return probabilities

def plot_probabilities(probabilities):
    sums = list(probabilities.keys())
    probs = list(probabilities.values())
    
    plt.figure(figsize=(10, 6))
    plt.bar(sums, probs, color='red')
    plt.xlabel('Сума')
    plt.ylabel('Ймовірність')
    plt.title('Ймовірність кожної суми при киданні двох кубиків')
    plt.xticks(sums)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.show()

def print_probabilities(probabilities):
    print("Ймовірності сум:")
    for sum_value, prob in sorted(probabilities.items()):
        print(f"Сума {sum_value}: {prob:.2%}")

num_rolls = 1000000
probabilities = simulate_dice_rolls(num_rolls)

print_probabilities(probabilities)
    
plot_probabilities(probabilities)
