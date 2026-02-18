# Create a class laptop with attributes: brand, RAM, price
# create 2 objects
# with diff values

class laptop:
    brand = "default"
    RAM = "8gb"
    Price = "1 lakh"

laptop1  = laptop()
laptop1.brand = "Acer"
laptop2 = laptop()
laptop2.brand = "Macbook"

print("Laptop1 brand:",laptop1.brand)
print("Laptop2 brand", laptop2.brand)