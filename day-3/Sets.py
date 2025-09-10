# Set example
fruits = {"apple", "banana", "cherry", "apple"}

print(fruits)  # {'banana', 'apple', 'cherry'}  (duplicates removed)

# Operations
fruits.add("mango")
fruits.remove("banana")

print("apple" in fruits)  # True
print("grapes" in fruits) # False
