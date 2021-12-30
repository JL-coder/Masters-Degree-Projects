def main():

    birth_rate = 8
    death_rate = 12
    immigrant_rate = 46
    number_of_seconds_per_day = 3600 * 24

    date_of_population = int(input("Please enter the population on 09/05/2019: "))
    total_number_of_days = int(input("Please enter the total number of days from 09/05/2019 to 09/06/2020: "))

    net_rate_per_second = 1/birth_rate + 1/immigrant_rate - 1/death_rate

    net_people_increased_per_day = net_rate_per_second * number_of_seconds_per_day

    date_of_future_population = date_of_population + (net_people_increased_per_day * total_number_of_days)

    print(int(date_of_future_population))

if __name__ == "__main__":
    main()