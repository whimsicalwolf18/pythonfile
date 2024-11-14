# Function to calculate the average of a list of numbers
def calculate_average(numbers):
    if len(numbers) == 0:  # Check if the list is empty
        return "List is empty, cannot compute average."
    
    total = sum(numbers)  # Sum all the numbers in the list
    average = total / len(numbers)  # Divide the total by the number of elements
    return average

# Example usage
numbers = [10, 20, 30, 40, 50]  # List of numbers
average = calculate_average(numbers)  # Calling the function
print(f"The average of the numbers is: {average}")
