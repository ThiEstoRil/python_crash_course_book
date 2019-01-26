motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)

motorcycles.append("ducati")
print(motorcycles)

motorcycles.insert(0, "ferrari")
print(motorcycles)

del motorcycles[0]
print(motorcycles)

popped_motorcycle = motorcycles.pop()
# Esto quita la última moto de la lista y la almacena en "popped_motorcycle"
# Puedo hacer lo mismo con cualquier posición añadiendo num: .pop(1)
print(motorcycles)
print(popped_motorcycle)

too_expensive = "yamaha"
motorcycles.remove(too_expensive)
print(motorcycles)
print("A " + too_expensive.title() + " is too expensive for me.")
