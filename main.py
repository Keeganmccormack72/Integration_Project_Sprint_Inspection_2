# Keegan McCormack
# This will be a calculator for dieting and notes of what I learned in COP 1500
def main():
    # It enters main for call back later near the end of the project
    print("Welcome to my Integration Project!")
    # Welcomes user to project
    continue_program = True
    # This will create a loop that will go on forever
    while continue_program:
        # The while statement shows when the value is not zero it will continue
        print("Enter the choice for what you would like to see")
        print("1. Shows how much your items will cost")
        print("2. Input dietary inputs to keep track for the day")
        print("0. Stop program")
        # Allows for the user to enter what they would like to do
        selection = int(input())
        # The users choice
        if selection == 1:
            # If they enter 1 it brings them to a cost calculator
            x = 0
            cost = float(input("Enter cost of Item"))
            while cost > 0:
                x = x + cost
                cost = float(input("Enter another items cost if done enter 0"))
            print("Cost: $" + cost)
        # This is a loop in which it adds up the cost of all items in the user
        # has until they enter zero
        elif selection == 2:
            calories = int(14000)
            fats = int(490)
            saturatedFats = int(140)
            carbohydrates = int(1820)
            totalSugars = int(630)
            protein = int(350)
            sodium = int(42)
            # Dietary fact for a week
            calories_day = calories / 7
            fats_day = fats / 7
            saturated_fats_day = saturatedFats / 7
            carbohydrates_day = carbohydrates / 7
            total_sugars_day = totalSugars / 7
            protein_day = protein / 7
            sodium_day = sodium / 7
            # variables calling for daily dietary facts
            repeat = true
            while repeat:
                itemName = input("Please enter the name of food:")
                inpCal1 = int(
                    input("Please enter the amount of calories(kcalories)"
                          " per serving size that is in item:"))
                inpFat1 = int(
                    input("Please enter the amount of fat per serving "
                          "size that is in this item:"))
                inpSat1 = int(
                    input("Please enter the amount of saturated fat per "
                          "serving size that is in this item:"))
                inpCarb1 = int(
                    input("Please enter the amount of Carbohydrates per "
                          "serving size that is in this item:"))
                inpSug1 = int(
                    input("Please enter the amount of sugar per serving "
                          "size that is in this item:"))
                inpPro1 = int(input("Please enter the amount of protein per "
                                    "serving size that is in this item:"))
                inpSod1 = int(
                    input("Please enter the amount of sodium per serving "
                          "size that is in this item:"))
                print("The amount of calories left after", itemName, "is"
                (calories - inpCal1), "for the week")
                print("For a single day it will be"(calories_day - inpCal1))
                # I made it so it would come out as an integer to better
                # understand the amount
                print("The amount of fats left after", itemName, "is"
                (fats - inpFat1), "for the week")
                print("For a single day it will be"(fats_day - inpFat1)),
                print("The amount of Saturated Fats left after", itemName,
                      "is "
                      (saturatedFats - Fat1), " for the week")
                print("For a single day it will be"
                      (saturated_fats_day - inpSat1)),
                print("The amount of carbohydrates left after", itemName, "is"
                (carbohydrates - inpCarb1), "for the week")
                print("For a single day it will be"(carbohydrates_day -
                                                    inpCarb1)),
                print("The amount of sugar left after", itemName, "is"
                (totalSugars - inpSug1), "for the week"),
                print("For a single day it will be"(total_sugars_day -
                                                    inpSug1)),
                print("The amount of protein left after", itemName, "is"
                (protein - inpPro1), "for the week")
                print("For a single day it will be"(protein_day - inpPro1)),
                print("The amount of sodium left after", itemName, "is"
                (sodium - inpSod1), "for the week")
                print("For a single day it will be"(sodium_day - inpSod1))
                stop = int(
                    input("If you would like to add another item enter any "
                          "number if you would like to stop input 0"))
        if stop != 0:
            itemName = input("Please enter the name of food:")
            inpCal1 = int(
                input("Please enter the amount of calories(kcalories)"
                      " per serving size that is in item: "))
            inpFat1 = int(input("Please enter the amount of fat per serving ")
                          ("size that is in this item:"))
            inpSat1 = int(input("Please enter the amount of saturated fat per "
                                "serving size that is in this item:"))
            inpCarb1 = int(
                input("Please enter the amount of Carbohydrates per "
                      "serving size that is in this item:"))
            inpSug1 = int(input("Please enter the amount of sugar per serving "
                                "size that is in this item:"))
            inpPro1 = int(input("Please enter the amount of protein per "
                                "serving size that is in this item:"))
            inpSod1 = int(
                input("Please enter the amount of sodium per serving "
                      "size that is in this item:"))
            print("The amount of calories left after", itemName,
                  "is "(calories - inpCal1), " for the week")
            print("For a single day it will be"(calories_day - inpCal1))
            # I made it so it would come out as an integer to better
            # understand the amount
            print("The amount of fats left after", itemName,
                  "is "(fats - inpFat1) + " for the week")
            print("For a single day it will be"(fats_day - inpFat1))
            print("The amount of Saturated Fats left after", itemName,
                  "is "(saturatedFats - Fat1), " for the week")
            print("For a single day it will be"(saturated_fats_day - inpSat1))
            print("The amount of carbohydrates left after", itemName,
                  "is"(carbohydrates - inpCarb1), "for the week")
            print("For a single day it will be"(carbohydrates_day - inpCarb1))
            print("The amount of sugar left after", itemName,
                  "is"(totalSugars - inpSug1), "for the week")
            print("For a single day it will be"(total_sugars_day - inpSug1))
            print("The amount of protein left after", itemName,
                  "is"(protein - inpPro1), "for the week")
            print("For a single day it will be"(protein_day - inpPro1))
            print("The amount of sodium left after", itemName,
                  "is"(sodium - inpSod1), "for the week")
            print("For a single day it will be"(sodium_day - inpSod1))
            stop = int(
                input("If you would like to add another item input 1 if "
                      "you would like to stop input 0"))
        else:
            repeat = false

        elif 0 == selection:
        continue_program = False
    else:
        print("Unknown Input. Try again")


main()
####Notes for other requirements for the project#####
fruit = input("Enter a word")
# The user can input a word
if fruit > "apple" and fruit < "pear":
    # It will see if that words is in alphabetical order compared to apple and
    # pear
    print(" valid")
    # If it is the program will print valid
else:
    # If it does not fit in alphabetical order
    print(" out of range")
    # It will then print our of range
a = float(input("Enter weight "))
# The users enter the weight of an object
b = float(input("Enter cost "))
# The user enters the cost of the same objects
print(a < 10 and b <= 20)
# The program checks to see if the weight is less than 10
# and the cost is less than 20
listing = input("Enter your favorite hobby: ")
# The user enters favorite hobby
for x in range(1, 5):
    # The program will list items 1 through 5 like a list
    print(str(x) + ".", listing, end="\t")
    # prints 1. input by user 2. input by user and so on till there are 5 of
    # them
