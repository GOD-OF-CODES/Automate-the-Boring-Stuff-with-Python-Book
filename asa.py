def print_combined_pyramid(rows):
    for i in range(1, rows + 1):
        print(" " * (rows - i) + "*" * (2 * i - 1))
    for i in range(rows - 1, 0, -1):
        print(" " * (rows - i) + "*" * (2 * i - 1))

# Taking user input for the height
try:
    rows = int(input("Enter the height of the pyramid: "))
    if rows <= 0:
        print("Please enter a positive integer for the height.")
    else:
        # Printing the combined pattern
        print_combined_pyramid(rows)
except ValueError:
    print("Invalid input! Please enter a positive integer.")
