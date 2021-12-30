import math

def main():
    #user_input_outer_radius = float(input("Please enter the outer circle radius: "))
    #user_input_inner_radius = float(input("Please enter the inner circle radius: "))

    #inner_area = (user_input_inner_radius ** 2) * math.pi
    #outer_area = (user_input_outer_radius ** 2) * math.pi
    #area = outer_area - inner_area

    #print("The area of the part between the inner circle and the outer circle is: ", area )
    #print("The rounded off area of the part between the inner circle and the outer circle is:", "%1.4f" % (area))
    #Can use the round function to acheive the same result as above
    #print("The rounded off area of the part between the inner circle and the outer circle is:", round(area,5))
    #one = 1
    #two = 2
    #print("1 > 2 is ", one > two)
    #print("2 > 1 is ", two > one)
    #print("1 > 1 is ", one > one)
    #print("1 < 2 is ", one < two)
    #print("2 < 1 is ", two < one)
    #print("1 < 1 is ", one < one)
    #print("1 >= 1 is ", one >= two)
    #print("2 >= 1 is ", two >= one)
    #print("1 >= 1 is ", one >= one)
    #print("1 <= 1 is ", one <= two)
    #print("2 <= 1 is ", two <= one)
    #print("1 <= 1 is ", one <= one)
    #print("1 == 1 is ", one == one)
    #print("1 == 2 is ", one == two)
    #print("1 != 1 is ", one != one)
    #print("1 != 2 is ", one != two)

    #Logical operator practice
    #print("True and True = ", True and True)
    #print("True and False = ", True and False)
    #print("False and True = ", False and True)
    #print("False and False = ", False and False)
    #print("True or True = ", True or True)
    #print("True or False = ", True or False)
    #print("False or True = ", False or True)
    #print("False or False = ", False or False)
    #print("not True = ", not True)
    #print("not False = ", not False)

    #Shortcut assignment practice
    #a = 5
    #a += 2
    #b = 5
    #b -= 2
    ##c = 5
    #c *= 2
    #d = 5
    #d /= 2
    #e = 5
    #e %= 2
    #g = 5
    #g **= 2
    #h = 5
    #h //= 2
    #print("5 += 2 is ",a)
    #print("5 -= 2 is ", b)
    #print("5 *= 2 is ", c)
    #print("5 /= 2 is ", d)
    #print("5 %= 2 is ", e)
    #print("5 **= 2 is ", g)
    #print("5 //= 2 is ", h)

    #Population Estimation Exercise my attempt
    user_input_pop = int(input("Enter US Population: "))
    sec = 3.15 * (10 ** 7)
    birth = sec / 8
    death = sec / 12
    migrant = sec / 670
    future_pop = ((user_input_pop + birth + migrant) - death)
    print("The future US popultation is: ", future_pop)

    #Answer to above
    birth_rate = 8
    death_rate = 12
    immigrant_rate = 670
    number_of_seconds_per_day = 24 * 60 * 60
    date_of_population = int(input("Please enter the population on 08/29/2020: "))
    total_number_of_days = int(input("Please enter the total number of days from 08/30/2020 to 08/29/2021: "))
    net_rate_per_second - 1 / birth_rate + 1 / immigrant_rate - 1 /death_rate
    net_people_increased_per_day = net_rate_per_second * number_of_seconds_per_day
    date_of_future_population = date_of_population + (net_people_increased_per_day * total_number_of_days)
    print(date_of_future_population)



if __name__ == "__main__":
    main()