fruit = ("apple", "banana", "orange", "grape", "kiwi")
print(fruit[2])
# Tuples are immutable, so you cannot update them
fruit.update([1] = "mango")
print(fruit)