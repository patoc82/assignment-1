# Bonus Challenge: Integrated Decision Tool

def is_profitable(revenue, cost):
    return revenue > cost


def get_category(category):
    # Remove extra spaces and convert to lowercase
    category = category.strip().lower()

    # Categorize the product
    if category == "electronics" or category == "gadget":
        return "High Margin"

    elif category.startswith("tech"):
        return "High Margin"

    elif category == "clothing" or category == "apparel":
        return "Medium Margin"

    elif category == "food" or category == "grocery":
        return "Low Margin"

    else:
        return "Uncategorized"


def main():
    # Get business information from the user
    revenue = float(input("What's the revenue? "))
    cost = float(input("What's the cost? "))
    category = input("What's the product category? ")

    # Determine the category
    margin_category = get_category(category)

    # Calculate profit
    profit = revenue - cost

    # Check if the business is profitable
    profitable = is_profitable(revenue, cost)

    # Display the results
    print()
    print(f"Profit: ${profit:,.2f}")
    print(f"Category: {margin_category}")

    if profitable:
        print("Business is profitable.")

        # Suggest an investment based on the category
        if margin_category == "High Margin":
            print("Recommendation: Reinvest.")

        elif margin_category == "Medium Margin":
            print("Recommendation: Consider expanding.")

        elif margin_category == "Low Margin":
            print("Recommendation: Review costs.")

        else:
            print("Recommendation: Review the business.")

    else:
        print("Business is not profitable.")
        print("Recommendation: Review costs and pricing.")


# Run the main function
main()