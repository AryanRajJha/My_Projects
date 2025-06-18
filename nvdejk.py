
# alpha =input("Enter your message:")
# print(alpha)

my_list = ["apple", "banana", "cherry"]

try:
    index = my_list.index("banana")
    print(f"Element found at index {index}")
except ValueError:
    print("Element not found")
