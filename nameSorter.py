#Hannah Edwards
'''
How to use:
In a linux terminal type
python3 /path of python file/ /path of sort me file/
There are no // needed around the file names
made sure that the path to the .txt file is in 'example.txt' (single quotes)
'''


import fileinput


def get_string_length(s):
    return len(s)


def print_list(names):
    for n in names:
        print(n)


def sort_names(names_list):
    # sort by length
    names_list.sort(key=get_string_length)

    # second/alphabetical sort within each length
    begin_at = 0
    i = 1
    sorted_list_of_names = []
    while i < len(names_list):
        if len(names_list[i]) > len(names_list[i - 1]):
            for n in sorted(names_list[begin_at:i]):
                sorted_list_of_names.append(n)
            begin_at = i
        i = i + 1
    for n in sorted(names_list[begin_at:len(names_list)]):
        sorted_list_of_names.append(n)

    return sorted_list_of_names

def reverse_sort_names(names_list_):
    return names_list.reverse()



# main function
# print('Searching for file')

cont = "0"
# welcome user with menu
while(cont == "0"):
    print("Welcome to name sorter, how would you like to sort your list?")
    print("1) By size (short to long) and alphabetically")
    print("2) By size (long to short) and reverse alphabetically")
    option = input("> ")
    while option != "1" and option != "2":
        print("Please enter a option number: 1 or 2")
        option = input("> ")

    # confirm output
    selected_option = "You have selected option {}."
    print(selected_option.format(option))

    # sort list of names option 1 way first
    names_list = []
    temp = ""
    for line in fileinput.input():
        temp = line.strip()
        if len(temp) > 0:
            names_list.append(temp)

    if option == "1":
        print_list(sort_names(names_list))

    else:
        names_list = sort_names(names_list)
        names_list.reverse()
        print_list(names_list)

    print("If you would like sort again, press '0'")
    cont = input(">")

print("GoodBye")

# sort list of names and print







