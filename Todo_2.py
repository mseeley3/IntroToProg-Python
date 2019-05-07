# --------------------------------#
# Title: "Todo_pt2"
# Dev: mseeley3
# Date: 5/6/19
# Changelog: (Who, When, What)
# mseeley3,5/6/19, Created Script
# find gihub repository here: https://github.com/mseeley3/IntroToProg-Python
# --------------------------------#

# -------------Data------------- #
# When the program starts, load the any data you have
# in a text file called ToDo.txt into a python Dictionary.
objFile = open("Todo.txt", "r")

# read each line of the text file and turn in into a list
strData = objFile.readlines()

# create an empty table
lstTable = []

# read the "strData" list
# use the for loop to add each line to the table lstTable as a dictionary

def step_1():
    for st in strData:
        # create a temporary list from the splitting the first element of lines
        # the readlines() function leaves a "\n" at the end, so we will scrub that with strip()
        # separate the task from the priority by "," using split()
        templine = st.strip("\n").split(",")

        # the first object in our templine is the task, store as "task"
        task = templine[0]

        # second object in our templine is the priority, store as "priority"
        priority = templine[1]

        # create a dictionary using task and priority
        dicRow = {"Task": task, "Priority": priority}

        # add dicRow to the empty table
        lstTable.append(dicRow)

step_1()

# -------------Input/Output------------- #
# User can see a Menu (Step 2)
# User can see data (Step 3)
# User can insert or delete data(Step 4 and 5)
# User can save to file (Step 6)

class manage_data(object):
    """This class contains method to managing the Todo database"""
    # Define the method
    @staticmethod

    # create a function to print out the user's options
    def step_2():
        print("""What would you like to do? Enter the number to the left of the action you would like to take.
        1: Show current data
        2: Add a new task
        3: Remove an existing task
        4: Save Data to File
        5: Exit Program""")

    # create a function to print out lstTable
    def step_3():
        print("**************************************************")

        for lst in lstTable:
            print(lst["Task"] + ": " + lst["Priority"])

        print("**************************************************")

    # create a function to add a new task
    def step_4():
        task = input("Enter a new task: ")
        priority = input("What is the priority level of this task?: ")

        tempdicRow = {"Task": task, "Priority": priority}

        lstTable.append(tempdicRow)

    # create a function to delete a task
    def step_5():
        # create a counter that starts as the first row of the table
        x = 0
        # create a value that matches how many row are in the table minus 2
        y = len(lstTable) - 2

        # get the task the user wants to delete
        search = input("Enter the task you want to delete (case sensitive): ")

        # this for loop will go through the lstTable row by row
        # it looks up the string under the key "Task" and try to match it to the input
        for task in lstTable:

            # if there is a match, the entire row will be removed from the table
            if (task["Task"] == search):

                # because the value of x matches which row the for loop is looking at
                # we can remove the whole row using .pop(x)
                lstTable.pop(x)

                # print out the table again so that the user can see their update
                print("'" + search + "'" + " has been removed.")

            # if the user enters a term that is not in the table
            # eventually the for lop will run more times than there are rows in the table
            # this will make x (the number of times the loop was run) greater than:
            # y (the number of rows in the table minus 2)
            # (it's a minus 2 instead of minus one, becaase python marks the 1st row as 0)
            # at that point we can tell the user their term was not found
            else:
                if (x > y):
                    print("That task was not found.")

            # for each run of the for loop, increase the counter by 1
            x = x + 1

    # create a function to save the data
    def step_6():
        # open the file
        Todo = open("Todo.txt", "w")

        # go down the tuple and store each row into the text file
        for lst in lstTable:
            # store the strings under each dictionary key as it's own object
            task = lst["Task"]
            priority = lst["Priority"]

            # store the data as "task" , "priority"
            Todo.write(str(task) + "," + str(priority) + "\n")

        # close connection to text file
        Todo.close

manage_data.step_2()

# -------------Processing------------- #
# create a while loop so that as long as the script is running
# this way the program will stay in this loop until the user is done
while (True):

    # Display a menu of choices to the user
    #manage_data.step_2()

    # if the user puts in something other than an integer number, we use this try-except construct to trap the error
    try:
        strChoice = int(input())

        if strChoice == 1:
            manage_data.step_3()

        elif strChoice == 2:
            manage_data.step_4()

        elif strChoice == 3:
            manage_data.step_5()

        elif strChoice == 4:
            manage_data.step_6()

        elif strChoice == 5:
            break  # and exit the program

        # if the user inputs a number greater than 5
        elif strChoice > 5:
            print("Wrong number.")

        # if the user inputs a number lower than 1
        elif strChoice < 1:
            print("Wrong number.")

    # print message telling the user that they can only put in a number 1-5
    except:
        print("Please enter a number that is from 1-5.")