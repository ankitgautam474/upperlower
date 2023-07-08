def count_upper_lower(input_str):
    upper_count = 0
    lower_count = 0

    for char in input_str:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1

    return upper_count, lower_count

# Get input from the user
input_str = input("Enter a string: ")

# Call the count_upper_lower function with the user input
upper_count, lower_count = count_upper_lower(input_str)

# Print the results
print("No. of Upper case characters:", upper_count)
print("No. of Lower case characters:", lower_count)
