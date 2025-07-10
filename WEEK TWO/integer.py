# Accept user input to create a list of integers and compute the sum
numbers = input("Enter a list of integers separated by spaces: ")
num_list = [int(x) for x in numbers.split()]
total = sum(num_list)
print(f"The sum of the numbers is: {total}")
