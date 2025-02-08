#Create a list of numbers and uses a loop to print even numbers 

numbers = [2,4,5,6,11,72,98]

for i in numbers:
    if i % 2 == 0:
        print(f"the number {i} is even")
    else:
        print(f"The number {i} is odd")