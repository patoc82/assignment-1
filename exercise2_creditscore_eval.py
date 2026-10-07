# Exercise 2: Credit Score Evaluator

# Get the credit score from the user
score = int(input("What's your credit score? "))

# Check if the score is within the valid range
if score < 300 or score > 850:
    print("Invalid score.")

elif score >= 750:
    print("Excellent - Loan Approved. Interest rate: Low")

elif score >= 700:
    print("Good - Loan Approved with Review. Interest rate: Low")

elif score >= 600:
    print("Fair - Loan Conditional. Seek credit improvement.")

else:
    print("Poor - Loan Denied. Seek credit improvement.")
