friends = ["andrew", "manolo", "rajoy"]
message = ", do you want to eat with me?"

print(friends[0].title() + message)
print(friends[1].title() + message)
print(friends[2].title() + message)

popped_friends = friends.pop(2)
print(popped_friends.title() + " can't come to dinner.")
friends.append("pepito")

print(friends[0].title() + message)
print(friends[1].title() + message)
print(friends[2].title() + message)

print("I have found a bigger dinner table.")

friends.insert(0, "pepa")
friends.insert(2, "pepo")
friends.append("ondraw")

print(friends[0].title() + message)
print(friends[1].title() + message)
print(friends[2].title() + message)
print(friends[3].title() + message)
print(friends[4].title() + message)
print(friends[5].title() + message)

print(friends)
