 # List Lab Starter
# Students: fill in code for Series 1–4 below


def series1():
    fruits = ["Apples", "Pears", "Oranges", "Peaches"]
    print("Series 1:", fruits)

    new_fruit = input("Enter a fruit to add to the list: ")
    fruits.append(new_fruit)
    print(fruits)

    fruit_number = int(input("Enter a number to display the corresponding fruit: ")) - 1
    print(f"You chose number {fruit_number + 1}, which is {fruits[fruit_number]}")

    fruits = ["Grapes"] + fruits
    print(fruits)

    fruits.insert(0, "Mango")
    print(fruits)

    print("Fruits that begin with P:")
    for fruit in fruits:
        if fruit[0].upper() == "P":
            print(fruit)

    return fruits
    # your code continues here


def series2():
    fruits = ["Apples", "Pears", "Oranges", "Peaches"]
    print("\nSeries 2:", fruits)
    fruits.pop()
    print("After removing the last fruit:", fruits)
    fruit_to_delete = input("Enter a fruit to delete: ").capitalize()
    if fruit_to_delete in fruits:
        fruits.remove(fruit_to_delete)
    print("After deletion:", fruits)
    fruits *= 2
    print("Doubled list:", fruits)
    while True:
        fruit_to_delete = input("Enter another fruit to delete (must exist): ").capitalize()
        if fruit_to_delete in fruits:
            fruits = [f for f in fruits if f != fruit_to_delete]
            break
        else:
            print("That fruit isn’t in the list. Try again.")

    print("After deleting all occurrences:", fruits)
    return fruits

    
    # your code continues here, "pass" allows you to test your code with incomplete functions
    pass


def series3():
    fruits = ["Apples", "Pears", "Oranges", "Peaches"]
    print("\nSeries 3:", fruits)
    fruits_copy = fruits[:]

    for fruit in fruits_copy[:]:
        while True:
            answer = input(f"Do you like {fruit.lower()}? (yes/no)")
            if answer == "no":
                fruits_copy.remove(fruit)
                break
            elif answer == "yes":
                break
            else:
                print("Please answer 'yes' or 'no'.")

    print("Fruits you like:", fruits_copy)
    return fruits_copy
    # your code continues here
    pass



def series4():
    fruits = ["Apples", "Pears", "Oranges", "Peaches"]
    print("\nSeries 4:", fruits)
    reversed_fruits = [fruit[::-1] for fruit in fruits]

    fruits.pop()

    print("Original list (with last item removed):", fruits)
    print("Reversed fruits list:", reversed_fruits)
    return fruits, reversed_fruits

    # your code continues here
    pass



def main():
    series1()
    series2()
    series3()
    series4()

# this just tells Python:
# "only run the code below if we are running THIS file directly"
# (not if another file tries to import this file)
# there is nothing to edit here
if __name__ == "__main__":
    main()
