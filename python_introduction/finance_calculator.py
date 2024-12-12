# User Input
monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your total monthly expenses: "))

# Calculate Monthly Savings
monthly_savings = monthly_income - monthly_expenses

# Annual Interest Rate (Simplified for Demonstration)
annual_interest_rate = 0.05  # 5%

# Projected Annual Savings (Simplified Formula)
projected_annual_savings = (monthly_savings * 12) + (monthly_savings * 12 * annual_interest_rate)

# Print Results
print(f"Your monthly savings are ${monthly_savings:.2f}.")
print(f"Projected savings after one year, with interest, is: ${projected_annual_savings:.2f}.")