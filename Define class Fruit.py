class Fruit:
    count = 0
    totalQuantity = 0

    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity
        Fruit.count += 1
        Fruit.totalQuantity += quantity

    def __str__(self):
        return f"{self.name} : {self.quantity}"

    def __del__(self):
        Fruit.count -= 1
        Fruit.totalQuantity -= self.quantity
N = int(input())
fruits = []
for ctr in range(N):
    name, quantity = input().split()
    fruit = Fruit(name, int(quantity))
    fruits.append(fruit)
print(Fruit.count)
print(Fruit.totalQuantity)
X = int(input())
del fruits[X-1]
for fruit in fruits:
    print(fruit)
print(Fruit.count)
print(Fruit.totalQuantity)