items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350},
}


def greedy_algorithm(items, budget):
    total_cost = 0
    total_calories = 0
    selected_items = []

    sorted_items = sorted(items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)



    for item, data in sorted_items:
        if total_cost + data['cost'] <= budget:
            selected_items.append(item)
            total_calories += data['calories']
            total_cost += data['cost']
    
    return selected_items, total_calories, total_cost


budget = 100
selected_items, total_calories, total_cost = greedy_algorithm(items, budget)
print("Вибрані страви:", selected_items)
print("Загальна калорійність:", total_calories)
print("Загальна вартість:", total_cost)


def dynamic_programming(items, budget):
    dp = [0] * (budget + 1)
    selected_items = [[] for _ in range(budget + 1)]

    for item, info in items.items():
        cost = info["cost"]
        calories = info["calories"]
        for current_budget in range(budget, cost - 1, -1):
            if dp[current_budget - cost] + calories > dp[current_budget]:
                dp[current_budget] = dp[current_budget - cost] + calories
                selected_items[current_budget] = selected_items[
                    current_budget - cost
                ] + [item]

    optimal_items = selected_items[budget]
    total_calories = dp[budget]

    return optimal_items, total_calories


selected_items, total_calories = dynamic_programming(items, budget)
print("\nДинамічне програмування")
print("Вибрані страви:", selected_items)
print("Загальна калорійність:", total_calories,"\n")