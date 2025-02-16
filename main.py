# task ...1 

names = ['Anastasia', 'Sasha', 'Nina', 'Mari', 'Qeti']

for name in names:
    print(name)
names = ['Anastasia', 'Sasha', 'Nina', 'Mari', 'Qeti']

# task ...2

for name in names:
    print(f"Hey, {name}! Hope you're doing well!")

# task ...3

cars = ['Porsche', 'Ferrari', 'Maybach', 'Maserati', 'Lamborghini']

for car in cars:
    print(f"I would like to own a {car} .")

# task ...4

guests = ['Kendrick Lamar', 'Kanye West', 'Playboi Carti']

for guest in guests:
    print(f"Dear {guest},\nI'm hosting a dinner this Friday. Your presence would be greatly appreciated.\n")

# task ...5

guests = ['Kendrick Lamar', 'Kanye West', 'Playboi Carti']

guests[2] = 'Young Thug'

for guest in guests:
    print(f"Dear {guest},\nI'm hosting a dinner this Friday. Your presence would be greatly appreciated.\n")

guests = ['Kendrick Lamar', 'Kanye West', 'Playboi Carti']

for guest in guests:
    print(f"Dear {guest},\nI'm hosting a dinner this Friday. Your presence would be greatly appreciated.\n")

print("Unfortunately, Playboi Carti cannot make it to the dinner.")

guests[2] = 'Young Thug'

print("\nUpdated Invitations:")

for guest in guests:
    print(f"Dear {guest},\nI'm hosting a dinner this Friday. Your presence would be greatly appreciated.\n")

# task ...6

guests = ['Kendrick Lamar', 'Kanye West', 'Playboi Carti']

for guest in guests:
    print(f"Dear {guest},\nI'm hosting a dinner this Friday. Your presence would be greatly appreciated.\n")

print("Unfortunately, Playboi Carti cannot make it to the dinner.")

guests[2] = 'Young Thug'

print("\nI found a bigger dinner table, so I have more space for guests!")

guests.insert(0, 'Travis Scott')  
guests.insert(2, 'Nas')  
guests.append('Metro Boomin')  

print("\nUpdated Invitations:")

for guest in guests:
    print(f"Dear {guest},\nI'm hosting a dinner this Friday. Your presence would be greatly appreciated.\n")

# task ...7

guests = ['Travis Scott', 'Kendrick Lamar', 'Kanye West', 'Nas', 'Young Thug', 'Metro Boomin']

for guest in guests:
    print(f"Dear {guest},\nI'm hosting a dinner this Friday. Your presence would be greatly appreciated.\n")

print("\nUnfortunately, my dinner table won't arrive in time, and I can only invite two guests.")

while len(guests) > 2:
    removed_guest = guests.pop()
    print(f"\nDue to unexpected circumstances, {removed_guest}, I regret that i won't be able to invite you to dinner")

for guest in guests:
    print(f"\nDear {guest},\nYou are still invited to dinner! See you there!")

del guests[:]

print("\nFinal guest list:", guests)


# task ...8

places = ['Lebanon', 'Morocco', 'Jordan', 'Egypt', 'Iran']

print("Original list:", places)

print("\nList in alphabetical order:", sorted(places))

print("\nOriginal list after sorted():", places)

print("\nList in reverse alphabetical order:", sorted(places, reverse=True))

print("\nOriginal list after reverse sorted():", places)

places.reverse()
print("\nList after reverse():", places)

places.reverse()
print("\nList after second reverse():", places)

places.sort()
print("\nList after sort() in alphabetical order:", places)

places.sort(reverse=True)
print("\nList after sort() in reverse alphabetical order:", places)

# task ...9 

guests = ['Travis Scott', 'Kendrick Lamar', 'Kanye West', 'Nas', 'Young Thug', 'Metro Boomin']

for guest in guests:
    print(f"Dear {guest},\nI'm hosting a dinner this Friday. Your presence would be greatly appreciated.\n")

print("\nUnfortunately, my dinner table won't arrive in time, and I can only invite two guests.")

while len(guests) > 2:
    removed_guest = guests.pop()
    print(f"\nDue to unexpected circumstances, {removed_guest}, I regret that i won't be able to invite you to dinner.")

for guest in guests:
    print(f"\nDear {guest},\nYou are still invited to dinner! See you there!")

print(f"\nI am inviting {len(guests)} guests to dinner.")



