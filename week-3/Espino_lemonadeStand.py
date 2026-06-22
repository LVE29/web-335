"""
Author: Leslie Espino
Date: June 21, 2026
File Name: Espino_lemonadeStand.py
Description: Calculates the cost and profit of running a lemonade stand.
"""

# Function to calculate the total cost
def calculate_cost(lemons_cost, sugar_cost):
    return lemons_cost + sugar_cost

# Function to calculate profit
def calculate_profit(lemons_cost, sugar_cost, selling_price):
    return selling_price - (lemons_cost + sugar_cost)

# Main function
# Variables
lemons_cost = 5
sugar_cost = 3
selling_price = 15

# Function calls
total_cost = calculate_cost(lemons_cost, sugar_cost)
profit = calculate_profit(lemons_cost, sugar_cost, selling_price)

# Output results
cost_output = str(lemons_cost) + " + " + str(sugar_cost) + " = " + str(total_cost)

profit_output = "Profit = " + str(profit)

print(cost_output)
print(profit_output)