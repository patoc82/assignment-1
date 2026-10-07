# Exercise 1: Profit Margin Calculator

# Get revenue and cost from the user
revenue = float(input("What's the revenue? "))
cost = float(input("What's the cost? "))

# Calculate profit
profit = revenue - cost

# Check that revenue is greater than zero before calculating margin
if revenue > 0:
    margin = (profit / revenue) * 100
    print(f"Profit: ${profit:,.2f} | Margin: {margin:.2f}%")
else:
    print("Invalid revenue.")