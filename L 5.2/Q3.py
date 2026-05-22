fruit1 = ["mango", "pineapple", "watermelon"]
fruit2 = ("mango", "pineapple", "watermelon")
print("List:", fruit1)
print("Tuple:", fruit2)
# Lists are mutable, so you can update them
fruit1[0] = "apple"
print("Updated List:", fruit1)
# Tuples are immutable, so you cannot update them
 fruit2[0] = "apple"
print("Updated Tuple:", fruit2)