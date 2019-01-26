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

print("The table will not be disponible tomorrow, so I can only invite 2 people.")

popped_friends = friends.pop()
print("Sorry, " + popped_friends.title() + ", you are not able to come to the dinner.")
popped_friends = friends.pop()
print("Sorry, " + popped_friends.title() + ", you are not able to come to the dinner.")
popped_friends = friends.pop()
print("Sorry, " + popped_friends.title() + ", you are not able to come to the dinner.")
popped_friends = friends.pop()
print("Sorry, " + popped_friends.title() + ", you are not able to come to the dinner.")

print(friends[0].title() + ", you are still invited to the dinner.")
print(friends[1].title() + ", you are still invited to the dinner.")

del friends[0]
del friends[0]

print(friends)
