# State income tax exercise

def main():
    # user_input = float(input("Enter your net income: "))
    # if user_input <= 15000:
    # print("No tax is paid on the first $15000 of net income.")
    # Dont need to say if net income is > 15000
    # elif user_input <= 30000:
    # print("A tax of 5% is assessed on each dollar of net income from 15k to 30k. ")
    # tax_paid = (user_input - 15000) * 0.05
    # print("You paid " + str(tax_paid) + " in taxes this year")
    # else:
    # print("A tax of 10% is assessed on each dollar of net income over 30k. ")
    # tax_paid = (15000 * 0.05) + (user_input - 30000) * 0.10
    # print("You paid " + str(tax_paid) + " in taxes this year")

    # Basketball Lead exercise
    #Note he was able to do it without the nested if statements. That said its not wrong to use them if you cant avoid it.
    #Nested if statements create multiple objects which can slow down the program.

    try:
        lead_input = int(input("Enter the lead in points: "))
        ball_input = str(input("Does the lead team have the ball? (Yes or No) ")).casefold()
        time_input = int(input("Enter the number of seconds left in the game: "))

        #One of the y/yes can be removed just keeping it so I can avoid the mistake I made while making this
        if (ball_input == 'yes' or ball_input == 'y') and lead_input >= 1 and time_input > 0:
            result = (lead_input - 3 + 0.5)
            if result > 0 and (result ** 2) > time_input:
                print("The lead is safe")
            else:
                print("The lead is not safe")

        elif (ball_input == 'no' or ball_input == 'n') and lead_input >= 1 and time_input > 0:
            result = (lead_input - 3 - 0.5)
            if result > 0 and (result ** 2) > time_input:
                print("The lead is safe")
            else:
                print("The lead is not safe")
        else:
            print("Invalid input please try again.")
    except ValueError:
        print("Invalid input please try again.")

if __name__ == "__main__":
    main()
