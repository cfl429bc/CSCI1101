

colors = {}
person = input("Enter person's name: ")
person = person.title()
favorite = input(f"Enter {person}'s favorite color: ")
favorite = favorite.lower()
colors[person] = favorite
print(colors)
