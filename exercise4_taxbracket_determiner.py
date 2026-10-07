# Exercise 4: Tax Bracket Determiner

def get_tax_bracket(income):
    # Check for invalid income
    if income < 0:
        return "Invalid income."

    # Determine the tax bracket
    elif income < 50000:
        return "Low (10%)"

    elif income < 100000:
        return "Medium (20%)"

    else:
        return "High (30%)"


# Ask the user for their income
income = float(input("What's your annual income? "))

# Get the tax bracket
bracket = get_tax_bracket(income)

# Calculate estimated tax based on the bracket
if income < 0:
    print(f"Your bracket: {bracket}")
elif income < 50000:
    estimated_tax = income * 0.10
    print(f"Your bracket: {bracket}. Estimated tax: ${estimated_tax:,.2f}")
elif income < 100000:
    estimated_tax = income * 0.20
    print(f"Your bracket: {bracket}. Estimated tax: ${estimated_tax:,.2f}")
else:
    estimated_tax = income * 0.30
    print(f"Your bracket: {bracket}. Estimated tax: ${estimated_tax:,.2f}")