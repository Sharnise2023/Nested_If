# Task 1:
attendees = int(input("Enter number of attendees: "))
venue = "large hall" if attendees > 100 else "conference room"
print(venue)

# Task 2:
attendees = int(input("Enter number of attendees: "))
venue = "large hall" if attendees > 100 else "conference room"
print(venue)

if attendees > 100:
    print("Recommendation: Use audio system and projector.")
elif 50 < attendees <= 100:
    print("Recommendation: Use a projector.")
else:
    print("Rocommendatiom: No additional equipment needed.")

# Task 3:
attendees = int(input("Enter number of attendees: "))
venue = "large hall" if attendees > 100 else "conference room"
print(venue)

if attendees > 100:
    print("Recommendation: Use audio system and projector.")
elif 50 < attendees <= 100:
    print("Recommendation: Use a projector.")
else:
    print("Rocommendatiom: No additional equipment needed.")

# Food preference
vegeterian = input("Do you want vegetarian food? (yes or no): ").strip().lower()
if vegeterian == "yes":
    print("Recommended caterer: Veggie Delight Caterers")
else:
    print('Recommended caterer: Gourmet Meals Caterers')
