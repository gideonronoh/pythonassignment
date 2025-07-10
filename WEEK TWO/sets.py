# Accept two sets of integers from the user
set1 = set(map(int, input("Enter integers for the first set (space-separated): ").split()))
set2 = set(map(int, input("Enter integers for the second set (space-separated): ").split()))

# Find common elements
common_elements = set1 & set2

print(f"Common elements: {common_elements}")
