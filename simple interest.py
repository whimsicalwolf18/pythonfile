# Function to calculate Simple Interest
def calculate_simple_interest(principal, rate, time):
    # Using the formula: SI = (P * R * T) / 100
    simple_interest = (principal * rate * time) / 100
    return simple_interest

# Example usage
principal_amount = float(input("Enter the principal amount: "))
rate_of_interest = float(input("Enter the rate of interest (in %): "))
time_period = float(input("Enter the time period (in years): "))

# Calculate the simple interest
simple_interest = calculate_simple_interest(principal_amount, rate_of_interest, time_period)

# Output the result
print(f"The Simple Interest is: {simple_interest:.2f}")
