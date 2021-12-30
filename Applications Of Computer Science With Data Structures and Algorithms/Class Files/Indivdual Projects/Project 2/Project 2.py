def main():
    filename = input("Please enter the name of your csv file: ")
    get_data = get_data_list(filename)
    monthly_average = get_monthly_average(get_data)
    highest,lowest = find_six_highest_lowest_monthly_average_price(monthly_average)
    reformatted_max_list = reformat_max_res(highest)
    reformatted_min_list = reformat_min_res(lowest)
    print_info(reformatted_max_list, reformatted_min_list)
#Opens the inputted data file and formats the dates into month/day/year
def get_data_list(file):
    csv_list = []

    #Open the file as read only and copy the information to a list line by line
    with open(file, "r") as file:
        csv_list = [row.strip().split(",") for row in file]

    #Add the year information to a seperate list ignoring the first line of information
    year_list = [line[0][0:4] for line in csv_list[1:]]

    #Using combination of for loop and enumrate to access the elements of the list and use replace method to remove
    #the years (with dashs - ), replace dashs with /, remove unnecessary 0s, and replace /0 with /. So that the dates
    #are properly formatted.
    for row in csv_list[1:]:
        for j, element in enumerate(row):
            row[j] = element.replace("2016-", "")
    for row in csv_list[1:]:
        for j, element in enumerate(row):
            row[j] = element.replace("2017-", "")
    for row in csv_list[1:]:
        for j, element in enumerate(row):
            row[j] = element.replace("2018-", "")
    for row in csv_list[1:]:
        for j, element in enumerate(row):
            row[j] = element.replace("2019-", "")
    for row in csv_list[1:]:
        for j, element in enumerate(row):
            row[j] = element.replace("2020-", "")
    for row in csv_list[1:]:
        for j, element in enumerate(row):
            row[j] = element.replace("-", "/")
    #Only replaces the first instance of 0 with a blank
    for row in csv_list[1:]:
        for j, element in enumerate(row):
            if row[j].startswith("0"):
                row[j] = element.replace("0", "", 1)
    #Only replaces the first instance of /0 with /
    for row in csv_list[1:]:
        for j, element in enumerate(row):
                row[j] = element.replace("/0", "/", 1)
    #Using the years from the year list add the years and a / to the end of the formatted row.
    for i, row in enumerate(csv_list[1:]):
        row[0] = row[0] + "/" + year_list[i]

    return csv_list

#Returns the average stock price for each month
def get_monthly_average(list_csv):
    #The number of days the stock market is open for each month. Found historical data and used it to populate the list.
    # Each line represents a years worth of days hence why the formatting is a little weird.
    day_list =        [19, 20, 22, 21, 21, 22, 20, 23, 21, 21, 21, 21,
                       20, 19, 23, 19, 22, 22, 20, 23, 20, 22, 21, 20,
                       21, 19, 21, 21, 22, 21, 21, 23, 19, 23, 21, 19,
                       21, 19, 21, 21, 22, 20, 22, 22, 20, 23, 20, 21,
                       21, 19, 22, 21, 20, 22, 22, 21, 21, 22, 20, 21]

    #Empty list to store formatted dates (without any duplicates)
    completed_date_list = []

    #Collect dates from csv list, ommitting the first row(line) and store in new date_list
    date_list = [line[0] for line in list_csv[1:]]

    #The dates are in string format so turn them into list format and store in new list (modifie_date_list) so that
    #they can be changed
    modified_date_list = [list(x) for x in date_list]

    #Loop through the modified list containing the string dates and check for presence of '/' depending on the location
    #del the slice containg at least one of the '/' and numbers.
    for date in modified_date_list:
        #Accounts for if the month starts with a single digit and has a single digit day i.e. 1/1/2016
        if date[1] == '/' and date[3] == '/':
            del date[1:3]
        #Accounts for if the month is single digit but, has multidigit days i.e. 1/16/2016
        elif date[1] == '/' and date[4] == '/':
            del date[1:4]
        #Accounts for if the month is multidigit but, has single digit days i.e. 11/1/2016
        elif date[2] == '/' and date[4] == '/':
            del date[2:4]
        #Accounts for if the month and day are both multidigit i.e. 11/11/2016
        else:
            del date[2:5]

    #Turn the list type dates back into string type
    rejoined_date_list = [''.join(sub_list) for sub_list in modified_date_list]

    #Remove duplicate dates from the list and store in a completed date list
    for dates in rejoined_date_list:
        if dates not in completed_date_list:
            completed_date_list.append(dates)

    #Collect volume data from csv file, type cast them into floats, and store in seperate list
    volume_list = [float(line[6]) for line in list_csv[1:]]
    #Collect adjacent close data from csv file, type cast them into floats, and store in seperate list
    adj_close_list = [float(line[5]) for line in list_csv[1:]]
    #Multiply each number from each list and store the result in a new list
    multiplied_list = [(number1 * number2) for number1, number2 in zip(volume_list, adj_close_list)]

    #Using the day list as an index (to create bounds based on how many days are in each month) create a new nested list
    #out of the multiplied list so that there are an appropriate amount of multiplied numbers for each month
    nested_multiplied_list = [multiplied_list[sum(day_list[:i]):sum(day_list[:i + 1])] for i in range(len(day_list))]

    #Sum the values in each nested list (i.e. take all the numbers in that one month and sum, leaving a nested list with
    # one number each).
    summed_list = list(map(sum, nested_multiplied_list))

    #Using the day list as an index (to create bounds based on how many days are in each month) create a new nested list
    # out of the volume list so that there are an appropriate amount of volume numbers for each month
    nested_volume_list = [volume_list[sum(day_list[:i]):sum(day_list[:i + 1])] for i in range(len(day_list))]

    #Sum the values in each nested list (i.e. take all the numbers in that one month and sum, leaving a nested list with
    # one number each).
    summed_volumes = list(map(sum, nested_volume_list))

    # Compute the monthly average stock price by taking the summed list and dividing it by the numbers in the summed
    # volume list. Store results in a new list
    computed_monthly_average = [(num1/num2) for num1,num2 in zip(summed_list, summed_volumes)]

    #Use 2 for loops and zip function to combine the dates from the completed date list and monthly stock averages from
    #the computed monthly average into one list in the desired format of date, stock average.
    completed_monthly_average = [a for b in zip(completed_date_list, computed_monthly_average) for a in b]

    # There are supposed to be 60 pairs of dates/stock average so create a list of length 60 populate it with the number
    # 2
    generated_list = [2 for num in range(60)]

    #Using the generated list as an index (to create bounds) create a nested list out of the completed monthly average
    #list where each nested list contains 2 entries
    completed_monthly_average = [completed_monthly_average[sum(generated_list[:i]):sum(generated_list[:i + 1])] for i in range(len(generated_list))]

    return completed_monthly_average

#Finds the six highest and lowest stock price among the data
def find_six_highest_lowest_monthly_average_price(monthly_average):

    #Generated list to be used to nest the created lists
    generated_list = [2 for num in range(6)]

    #Collect average stock price from monthly average list
    values_list = [sublist[1] for sublist in monthly_average]

    #Collect dates from monthly average list
    date_list = [sublist[0] for sublist in monthly_average]

    #Taking advantage of the fact that there are no duplicates in the values list I can use the sort method to easily
    #get the maximum/min values in order
    sorted_values = sorted(values_list)
    #Slice the list so only the last 6 values are collected and reverse the list so it appears in descending order
    max_sorted_values = sorted(values_list)[-6:]
    max_sorted_values.reverse()

    #Collect the index of the max values from the max sorted values list
    max_index_list = [values_list.index(values) for values in max_sorted_values]
    #Use the index of the max values to find the corresponding dates to the max value
    max_date_list = [date_list[index] for index in max_index_list]

    #Combine the date and values list so that they appear in proper format (date, value)
    highest_average_price = [a for b in zip(max_date_list, max_sorted_values) for a in b]

    #Using the generated list as the bounds create a nested list containing one date/value combo per nested list
    nested_highest_average_price = [highest_average_price[sum(generated_list[:i]):sum(generated_list[:i + 1])] for i in
                                   range(len(generated_list))]

    #Collect the first 6 values reprsenting the lowest stock price from the values list
    min_sorted_values = sorted(values_list)[:6]

    # Collect the index of the min values from the min sorted values list
    min_index_list = [values_list.index(values) for values in min_sorted_values]

    # Use the index of the min values to find the corresponding dates to the min value
    min_date_list = [date_list[index] for index in min_index_list]

    # Combine the date and values list so that they appear in proper format (date, value)
    lowest_average_price = [a for b in zip(min_date_list, min_sorted_values) for a in b]

    # Using the generated list as the bounds create a nested list containing one date/value combo per nested list
    nested_lowest_average_price = [lowest_average_price[sum(generated_list[:i]):sum(generated_list[:i + 1])] for i in
                                    range(len(generated_list))]

    return [nested_highest_average_price, nested_lowest_average_price]

#Changes the date format for the highest stock prices from numerical to alphabetical i.e. 11/2020 to Nov 2020
def reformat_max_res(nested_highest_average_price):
    #List of months that I use to replace the number equivelents
    month_list = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec']

    #Collect the dates from the list passed into the function
    modified_date_list = [sublist[0] for sublist in nested_highest_average_price]

    #Collect the average stock price from the list passed into the function and round them to 2 decimal places
    values_list = [round(sublist[1],2) for sublist in nested_highest_average_price]

    #Turn the string dates into list dates so that they can be modified
    modified_date_list = [list(date) for date in modified_date_list]

    #Loop through the date list and replace the numbered months with their respective non-numerical equivelent
    for char in modified_date_list:
        if char[0] == '1' and char[1] == '2':
            char[0:2] = month_list[11]
            char[3] = " "
            char.append(':')
        elif char[0] == '1' and char[1] == '1':
            char[0:2] = month_list[10]
            char[3] = " "
            char.append(':')
        elif char[0] == '1' and char[1] == '0':
            char[0:2] = month_list[9]
            char[3] = " "
            char.append(':')
        elif char[0] == '9':
            char[0] = month_list[8]
            char[1] = " "
            char.append(':')
        elif char[0] == '8':
            char[0] = month_list[7]
            char[1] = " "
            char.append(':')
        else:
            char[0] = month_list[6]
            char[1] = " "
            char.append(':')
    # Turn the list type dates back into string type dates
    rejoined_date_list = [''.join(sub_list) for sub_list in modified_date_list]

    #Recombine the dates and rounded average stock price values in correct order
    reformatted_list = [a for b in zip(rejoined_date_list, values_list) for a in b]

    # Generated list to be used to nest the created lists
    generated_list = [2 for num in range(6)]

    # Using the generated list as the bounds create a nested list containing one date/value combo per nested list
    reformatted_list = [reformatted_list[sum(generated_list[:i]):sum(generated_list[:i + 1])] for i in
                        range(len(generated_list))]

    return reformatted_list

#Changes the date format for the lowest stock prices from numerical to alphabetical i.e. 11/2020 to Nov 2020
def reformat_min_res(nested_lowest_average_price):
    # List of months that I use to replace the number equivelents
    month_list = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec']

    # Collect the dates from the list passed into the function
    modified_date_list = [sublist[0] for sublist in nested_lowest_average_price]

    # Collect the average stock price from the list passed into the function and round them to 2 decimal places
    values_list = [round(sublist[1], 2) for sublist in nested_lowest_average_price]

    # Turn the string dates into list dates so that they can be modified
    modified_date_list = [list(date) for date in modified_date_list]

    # Loop through the date list and replace the numbered months with their respective non-numerical equivelent
    for char in modified_date_list:
        if char[0] == '1':
            char[0] = month_list[0]
            char[1] = " "
            char.append(':')
        elif char[0] == '2':
            char[0] = month_list[1]
            char[1] = " "
            char.append(':')
        elif char[0] == '3':
            char[0] = month_list[2]
            char[1] = " "
            char.append(':')
        elif char[0] == '5':
            char[0] = month_list[4]
            char[1] = " "
            char.append(':')
        elif char[0] == '6':
            char[0] = month_list[5]
            char[1] = " "
            char.append(':')
        else:
            char[0] = month_list[6]
            char[1] = " "
            char.append(':')

    # Turn the list type dates back into string type
    rejoined_date_list = [''.join(sub_list) for sub_list in modified_date_list]
    reformatted_list = [a for b in zip(rejoined_date_list, values_list) for a in b]

    # Generated list to be used to nest the created lists
    generated_list = [2 for num in range(6)]

    # Using the generated list as the bounds create a nested list containing one date/value combo per nested list
    reformatted_list = [reformatted_list[sum(generated_list[:i]):sum(generated_list[:i + 1])] for i in
                        range(len(generated_list))]

    return reformatted_list

#Prints the six highest and lowest averge stock prices
def print_info(max_list, min_list):
    print("Google Stock Prices Between Jan 01, 2016 and Dec 31, 2020")
    print("")
    print("Six Highest Monthly Average Prices:")
    #Collect and store stock prices as strings in a list
    converted_maxvalues_list = [str(values[1]) for values in max_list]
    #Collect dates and store in a list
    max_date_list = [values[0] for values in max_list]
    #Recombine the date and stock price lists (so that now they are all strings)
    max_reformatted_list = [a for b in zip(max_date_list, converted_maxvalues_list) for a in b]
    #Loop through the ranged length of the recombined list, skipping every other entry, and combine the
    # leading and next entry into a single entry. Store in a merged list.
    max_merged_list = [max_reformatted_list[i] + " " + max_reformatted_list[i + 1] for i in range(0, len(max_reformatted_list)-1, 2)]

    #Print the strings from the list
    for sub_list in max_merged_list:
        print(sub_list)

    # Collect and store stock prices as strings in a list
    converted_minvalues_list = [str(values[1]) for values in min_list]
    # Collect dates and store in a list
    min_date_list = [values[0] for values in min_list]
    # Recombine the date and stock price lists (so that now they are all strings)
    min_reformatted_list = [a for b in zip(min_date_list, converted_minvalues_list) for a in b]
    # Loop through the ranged length of the recombined list, skipping every other entry, and combine the
    # leading and next entry into a single entry. Store in a merged list.
    min_merged_list = [min_reformatted_list[i] + " " + min_reformatted_list[i + 1] for i in
                   range(0, len(min_reformatted_list) - 1, 2)]
    print("")
    print("Six Lowest Monthly Average Prices:")
    # Print the strings from the list
    for sub_list in min_merged_list:
        print(sub_list)

if __name__ == "__main__":
    main()