def generate_profile(age: int) -> str:
    """Determine a person's life stage.

    :param age: Current person's age.
    :return: Name of a life stage.
    """
    if 0 <= age <= 12:
        return "Child"
    elif 13 <= age <= 19:
        return "Teenager"
    elif 20 <= age:
        return "Adult"


user_name = input("Enter your full name: ")
birth_year_str = input("Enter your birth year: ")
birth_year = int(birth_year_str)
current_year = 2025
current_age = current_year - birth_year

hobbies = []

while True:
    temp_entry = input("Enter a favorite hobby or type 'stop' to finish: ")
    if temp_entry.lower() != "stop":
        hobbies.append(temp_entry)
    else:
        break

life_stage = generate_profile(current_age)

user_profile = {"name": user_name, "age": current_age, "stage": life_stage, "hobbies": hobbies}

print("")
print("---")
print("Profile Summary:")
print(f"Name: {user_profile['name']}")
print(f"Age: {user_profile['age']}")
print(f"Life Stage: {user_profile['stage']}")

if len(user_profile["hobbies"]) > 0:
    print(f"Favorite Hobbies ({len(user_profile['hobbies'])}):")
    for i in user_profile["hobbies"]:
        print(f"- {i}")
else:
    print("You didn't mention any hobbies.")

print("---")