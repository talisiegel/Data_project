name = input("What is your name? ")
print(f"Hello, {name}! Nice to meet you.")

age_str = input(f"{name}, how old are you? ")
age = int(age_str)

if age > 18:
    job = input("What is your job? ")
    print(f"{job} sounds fun! Good luck with it, {name}!")
else:
    print("Do you like Sophia the First?")
    sophia = input("> ").strip().lower()

    if sophia == "yes":
        print("That's awesome! Sophia the First is a great show!")
        print("Maybe you can be a princess (or prince) someday too!")
    else:
        print("Do you like Paw Patrol?")
        paw_patrol = input("> ").strip().lower()
        if paw_patrol == "yes":
            print("Paw Patrol is super cool! Chase is on the case!")
        else:
            print("That’s okay! Maybe you prefer reading or playing outside!")
