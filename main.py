#imports the random module
import random


# asks the user how many dials they want in each lock combination
# ex. if user entered 5, the output could be:  1 0 8 8 2 
# checks whether the user's input is 3 or less
# if less than 3, it would restart the program, causing them to pick values until the value is 3 or more
def get_number_of_dials():
    num_dials = int(input("How many dials should each lock have? "))
    if num_dials >= 3: 
        return num_dials   
    else:
        print("You must enter of a value of 3 or greater!")
        get_number_of_dials()
        return num_dials
    

# stores how many dials the user wants in a global variable by calling previous function
num_dials = get_number_of_dials()



# prompts user for how many lock combinations they would like
# ex. if user enter 2, the program would print:
# Number 1: 1 0 8 8 2
# Number 2: 5 2 3 5 1
def get_how_many_to_list():
    return int(input("How many lock combinations should be generated? "))

# stores how many lock combos the user wants in a global variable by calling previous fucntion
num_lock_combos = get_how_many_to_list()



# function will return random int which falls between min num and max num INCLUSIVE
# used to define the range for which the combinations will be made from
# ex. if the arguements are 3 and 7:
# the lock combiantion can include numbers from 3 to 6(inclusive)
def get_number(min_num, max_num):
    return random.randrange(min_num, max_num)



#function will produce and print the lock combinations
# takes in 2 paramenters: 
# 1) the number of dials the user wants
# 2) the number of lock combos the user wants
def next_combo_number(num_dials, num_lock_combos):
    # to store ALL the lock combos
    all_combos = []

    # creates the number of lock combos
    for i in range(num_lock_combos):
        # to store an individual lock combo
        combo = ""

        # creates the number of dials the user wants and adds into a string
        for x in range(num_dials):
           combo = combo+" "+str(get_number(0,10))

        #adds the single combo to a list with all the combos
        all_combos.append(combo) 
    
    # prints the lock combos 
    for j in range(len(all_combos)):
        print("Number " + str(j + 1) + ": " + str(all_combos[j]))
    print("--------------------------------------")
    print("Here are " + str(num_lock_combos) + " random lock combinations")

# calls the previous functions with return values of 2 other functions as arguements
next_combo_number(num_dials, num_lock_combos)
