hello = "bonjour"
thisList = [3, "hello", hello, 4.3, 3 + 3j, False]
list_tuple = tuple(thisList)
print(list_tuple)
# CANNOT CHANGE LIST TO RANGE BECAUSE THE INPUT MUST BE INTEGER

thistuple = (3, "hello", hello, 4.3, 3 + 3j, False)
tuple_list = list(thistuple)
print(tuple_list)
# CANNOT CHANGE TUPLE TO RANGE BECAUSE THE INPUT MUST BE INTEGER

thisRange = range(1, 6, 2)
range_tuple = tuple(thisRange)
print(range_tuple)
range_list = list(thisRange)
print(range_list)
# CAN CHANGE RANGE TO LIST AND TUPLE