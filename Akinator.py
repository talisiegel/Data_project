name = input("What is your name? ")
print(f"Hello, {name}! Nice to meet you. Remember to only use lowercase letters")

age_str = input(f"{name}, how old are you? ")
age = int(age_str)

if age > 18:
    job_str = input("What is your job? ")
    print(f"{job_str} sounds fun! Good luck, {name}!")

else:
    print("Do you like Sophia the First?")
    sophia = input("> ")

    if sophia == "yes":
        print("Do you watch on an iPad?")
        ipad = input("> ")

        if ipad == "yes":
            print("Ok. Go watch on your iPad, see you later!")
        else:
            print("Do you watch on your TV?")
            tv = input("> ")

            if tv == "yes":
                print("Ok! Have fun watching on your TV!")
            else:
                print("Do you watch on your phone?")
                phone = input("> ")

                if phone == "yes":
                    print("Have fun watching on your phone!")
                else:
                    print("You are lying about something, so I am done with you!")
    else:
        print("Do you like Paw Patrol?")
        paw_patrol = input("> ")

        if paw_patrol == "yes":
            print("Paw Patrol is super cool! Chase is on the case!")
        elif paw_patrol == "maybe":
            print("You are the leader of all childern. I bow down to you.")
        else:
            while True:
                childhood = input("Did you have a childhood? ")
                if childhood == "no":
                    print("Oh... that’s unfortunate. Moving on then.")
                    break
