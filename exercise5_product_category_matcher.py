# Exercise 5: Product Category Matcher

# Prompt the user for a product name
product = input("What's the product name? ")

# Remove extra spaces and convert to lowercase
product = product.strip().lower()

# Categorize the product
if product == "electronics" or product == "gadget":
    category = "High Margin"

elif product.startswith("tech"):
    category = "High Margin"

elif product == "clothing" or product == "apparel":
    category = "Medium Margin"

elif product == "food" or product == "grocery":
    category = "Low Margin"

else:
    category = "Uncategorized - Review Needed"

# Print the result
print(f"Product: {product} | Category: {category}")