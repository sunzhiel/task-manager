# This is a task management application designed for a small business.
# It works with 2 text files in which are stored user login details &
# allocated tasks respectively. The program can read & write data
# from & to these files. It can also generate 2 additional text files
# for reporting user & task statistics.

# Import required libraries.
import datetime

import os.path

global username
# Define reg_user function for registering new users.
def reg_user():
    admin = admin_priviledge()
    login_details = user_tracker()
    if admin == True:
        print()
        new_user = input("Please enter a username for the new user: ")
        print()
        while True:
    # Make sure duplicate user names are not allowed.
            if new_user in login_details:
                print("This username is already in use. Try again")
                print()
                new_user = input("Please enter a username for the new user: ")
            else:
                new_pass = input(f"Please enter a password for {new_user}: ")
                pass_check = input("Please type in the password again: ")
                print()
                while True:
    # Check that new password is confirmed accurately.
                    if new_pass != pass_check:
                        print("The passwords do not match! Try again")
                        print()
                        new_pass = input(f"Please enter a password for {new_user}: ")
                        pass_check = input("Please type in the password again: ")
                    else:
                        print()
                        print(f"New user {new_user} added!")
                        print()
        

    # Write new user login details to user text file.
                        with open("user.txt", "a") as user_reg:
                            user_reg.write("\n")
                            user_reg.write(f"{new_user}, {new_pass}")
                            break
                break         
    else:
        print() 
        print(f"You do not have admin privileges, {username}! Try something else.")
        print()

# Define add_task function for assigning new tasks.
def add_task():
    print()
    assignee = input("Please enter the username of the person you are assigning this to: ")
    print()
    task_title = input("Enter a title for the task: ")
    print()
    description = input("Please enter a description of the task: ")
    print()

    # Get the current date using datetime module and format as appropriate.
    date_today = datetime.date.today()
    date_assigned = date_today.strftime("%d %b %Y")
    print(f"Today\'s date is {date_assigned}.")
    print()
    due_date = input("Please enter the task due date in the format dd mmm yyyy: ")
    task_status = "No"

    # Write new task details to tasks text file in the prescribed format.
    with open("tasks.txt", "a") as new_task:
        new_task.write("\n")
        new_task.write(f"{assignee}, {task_title}, {description}, {date_assigned}, {due_date}, {task_status}")
        #Display confirmation that task has been assigned.
        print()
        print(f"{task_title} has been assigned to {assignee}!")
        print()

# Define view_all function for viewing all listed tasks.
def view_all():
    print()
    task_count = 0
    task_list = []
    tasks = task_tracker()
    for key in tasks:
        task_count += 1
        task_list.append(str(key))
        print(f"Task ref: {key}")
        print("________________________________________________________")
        print(f"Task:            {tasks[key]['task_title']}")
        print(f"Assigned to:     {tasks[key]['assignee']}")
        print(f"Date assigned:   {tasks[key]['date_assigned']}")
        print(f"Due date:        {tasks[key]['due_date']}")
        print(f"Task complete?   {tasks[key]['task_status']}")
        print("Task description:")
        print(f"  {tasks[key]['description']}")
        print("________________________________________________________")
        print()

    print(f"Active task numbers are: {task_list}")

# Define view_mine function for viewing all tasks assigned to the logged in user.
def view_mine():
    print()
    task_count = 0
    user_task_list = []
    tasks = task_tracker()
    for key in tasks:
        if username == tasks[key]["assignee"]:
            task_count += 1
            user_task_list.append(str(key))
            print(f"Task ref: {key}")
            print("________________________________________________________")
            print(f"Task:            {tasks[key]['task_title']}")
            print(f"Assigned to:     {tasks[key]['assignee']}")
            print(f"Date assigned:   {tasks[key]['date_assigned']}")
            print(f"Due date:        {tasks[key]['due_date']}")
            print(f"Task complete?   {tasks[key]['task_status']}")
            print("Task description:")
            print(f"  {tasks[key]['description']}")
            print("________________________________________________________")
            print()

    if task_count > 0:
       print(f"{username}, you have {task_count} tasks assigned to you!")
       print(f"Your task numbers are: {user_task_list}")
       print("________________________________________________________") 
       print()
       task_to_edit = input("Please select a task to edit by entering its reference number or enter -1 to return to the main menu: ")
       while True:
            if task_to_edit != "-1" and task_to_edit not in user_task_list:
                print()
                print("You did not select a task allocated to you! Please try again.")
                print()
                task_to_edit = input("Please select a task to edit by entering its reference number or enter -1 to return to the main menu: ")
                print()
            elif task_to_edit != "-1" and task_to_edit in user_task_list:
                selection = int(task_to_edit)
                task_edit(selection)
                break
            
            elif task_to_edit == "-1":
                break
            break

    if task_count == 0:
        print(f"{username}, you have no tasks assigned to you!")
        print()

# Create a dictionary of lists to be called with the user_tracker function.
def user_tracker():
    user_list = []
    login_details = {}
    with open("user.txt", "r") as user_set:
        for num, line in enumerate(user_set):
            user_list_prep = line.strip("\n")
            user_list = user_list_prep.split(", ")
            login_details[num + 1] = {"username": user_list[0], "password": user_list[1]}
    return login_details

# Create login function.
def login():
    # Create global variable "username" to be accessed by multiple functions.
    global username
    login_details = user_tracker()
    passcode = 0

# Request user to login.
    username = input("Please enter your username: ")
    password = input("Please enter your password: ")
    print()

# Make sure that username and password are the correct key/value pair.
    for key in login_details:
        if (username == login_details[key]["username"]) and (password == login_details[key]["password"]):
            passcode += 1

# Use while loop to users are guided to provide correct
# login details. Display error messages if otherwise.
    while True:
        if passcode == 0:
            print("You entered an invalid username and/or password! Try again.")
            print()
            username = input("Please enter your username: ")
            password = input("Please enter your password: ")
            print()
            for key in login_details:
                if username == login_details[key]["username"] and password == login_details[key]["password"]:
                    passcode += 1

    
        elif passcode == 1:
            print(f"Login successful. Welcome, {username}!")
            print()
            break


# Create a dictionary of lists to be called with the task_tracker function.
def task_tracker():
    task_list = []
    task_dict = {}
    with open("tasks.txt", "r") as task_set:
        for num, line in enumerate(task_set):
            task_list_prep = line.strip("\n")
            task_list = task_list_prep.split(", ")
            task_dict[num + 1] = {"assignee": task_list[0], "task_title": task_list[1], "description": task_list[2], "date_assigned": task_list[3], "due_date": task_list[4], "task_status": task_list[5]}
    return task_dict

def task_edit(selection):
    tasks = task_tracker()
    # Display a menu for selecting tasks to edit.
    task_option = input('''Select one of the following options below:
    1 - mark task as complete
    2 - edit task
    3 - return to main menu
    : ''')
    while True:
        if task_option != "1" and task_option != "2" and task_option != "3":
            print("You entered an invalid selection. Please try again.")
            task_option = input('''Select one of the following options below:
            1 - mark task as complete
            2 - edit task
            3 - return to main menu
            : ''')

        elif task_option == "1":
            if tasks[selection]["task_status"] == "Yes":
                print(f"Task {selection} was already marked as completed!")
                print()
                break
            

            elif tasks[selection]["task_status"] == "No":
                tasks[selection]["task_status"] = "Yes"
                re_task(tasks)
                print(f"Task {selection} has now being marked as completed!")
                print()
                break

        elif task_option == "2":
            if tasks[selection]["task_status"] == "Yes":
                print(f"Task {selection} is already marked as completed and cannot be edited!")
                print()
                break

            elif tasks[selection]["task_status"] == "No":
                edit_option = input('''Select one of the following options below:
                4 - edit the user that the task is assigned to
                5 - edit the task due date
                6 - return to main menu
                : ''')

                while True:
                    if edit_option != "4" and edit_option != "5" and edit_option != "6":
                        print("You entered an invalid selection. Please try again.")
                        edit_option = input('''Select one of the following options below:
                        4 - edit the user that the task is assigned to
                        5 - edit the task due date
                        6 - return to main menu
                        : ''')

                    elif edit_option == "4":
                        new_assignee = input("Please enter the username of the person you are reassigning the task to: ")
                        tasks[selection]["assignee"] = new_assignee
                        print()
                        re_task(tasks)
                        print(f"Task {selection} has now been re-assigned to {new_assignee}.")
                        print()
                        break

                    elif edit_option == "5":
                        new_due_date = input("Please enter the new due date for the task in the format dd mmm yyyy: ")
                        tasks[selection]["due_date"] = new_due_date
                        print()
                        re_task(tasks)
                        print(f"Task {selection} has now been given a new due date of {new_due_date}.")
                        print()
                        break

                    elif edit_option == "6":
                        break

        elif task_option == "3":
            break    
        break

# Create re_task function for overwriting tasks text file with new task details.
def re_task(tasks):
    with open("tasks.txt", "w") as re_task:
                    for key in tasks:
                        new_line = "\n"
                        re_task.write(f"{tasks[key]['assignee']}, {tasks[key]['task_title']}, {tasks[key]['description']}, {tasks[key]['date_assigned']}, {tasks[key]['due_date']}, {tasks[key]['task_status']}")
                        re_task.write(new_line)

# Create display_statistics function for displaying high level overviews when admin is logged in.
def display_statistics():
    if admin == True:
        print()
        if not os.path.exists("task_overview.txt") and not os.path.exists("user_overview.txt"):
            generate_reports()
            
        with open("task_overview.txt", "r") as task_data:
            task_overview = task_data.read()
            print("Task Overview")
            print(task_overview)
            print()
            
        with open("user_overview.txt", "r") as user_data:
            user_overview = user_data.read()
            print("User Overview")
            print(user_overview)

# Discourage any users trying to access secret menu options.
    else:
        print() 
        print(f"You do not have admin privileges, {username}! Try something else.")
        print()

# Create generate_reports function for cooking up reports!
def generate_reports():
    total_tasks = 0
    complete_tasks = 0
    incomplete_tasks = 0
    overdue_tasks = 0
    incomplete_percentage = 0.0
    overdue_percentage = 0.0

    tasks = task_tracker()
    for key in tasks:
        total_tasks += 1
        if tasks[key]["task_status"] == "Yes":
            complete_tasks += 1
        elif tasks[key]["task_status"] == "No":
            incomplete_tasks += 1

# Create datetime objects from values stored at the key due_date to work out what is overdue.
        datetime_obj = datetime.datetime.strptime(tasks[key]["due_date"], "%d %b %Y")
        date_today = datetime.datetime.today()
        if (datetime_obj < date_today and tasks[key]["task_status"] == "No"):
            overdue_tasks += 1

    # Avoid errors arising from trying to divide by zero.        
    if total_tasks != 0:
        incomplete_percentage = round(((incomplete_tasks / total_tasks) * 100), 2)
        overdue_percentage = round(((overdue_tasks / total_tasks) * 100), 2)

    # Write the data to a new text file "task_overview" to be viewed as a report. 
    with open ("task_overview.txt", "w") as task_overview:
        task_overview.write(f"The total number of tasks that have been assigned in the task manager: {total_tasks}\n")
        task_overview.write(f"The total number of completed tasks: {complete_tasks}\n")
        task_overview.write(f"The total number of uncompleted tasks: {incomplete_tasks}\n")
        task_overview.write(f"The total number of overdue tasks: {overdue_tasks}\n")
        task_overview.write(f"The percentage of incomplete tasks: {incomplete_percentage}%\n")
        task_overview.write(f"The percentage of overdue tasks: {overdue_percentage}%")
    print()

    tasks_total = 0
    users_total = 0

    tasks = task_tracker()
    users = user_tracker()

    for task in tasks:
        tasks_total += 1
        
    for user in users:
        users_total += 1
        
    # Write the data to a new text file "user_overview" to be viewed as a report.
    with open ("user_overview.txt", "w") as user_overview:
        user_overview.write(f"The total number of users registered with task_manager: {users_total}\n")
        user_overview.write(f"The total number of tasks that have been assigned in the task manager: {tasks_total}\n")
        user_overview.write("\n")

    for user in users:
        user_tasks = 0
        user_complete = 0
        user_incomplete = 0
        user_overdue = 0
        user_complete_percent = 0.0
        user_incomplete_percent = 0.0
        user_overdue_percent = 0.0

    # Initiate a nested loop to loop through the dictionaries "users" and "tasks".
        for task in tasks:
            if users[user]["username"] == tasks[task]["assignee"]:
                user_tasks += 1
                if tasks[task]["task_status"] == "Yes":
                    user_complete += 1
                if tasks[task]["task_status"] == "No":
                    user_incomplete += 1
    # Create datetime objects from values stored at the key due_date to work out what is overdue.
                datetime_obj = datetime.datetime.strptime(tasks[task]["due_date"], "%d %b %Y")
                date_today = datetime.datetime.today()
                if (datetime_obj < date_today and tasks[task]["task_status"] == "No"):
                    user_overdue += 1
                
    # Avoid errors arising from trying to divide by zero.
        if tasks_total != 0:
            user_tasks_percent = round(((user_tasks / tasks_total) * 100), 2)

        if user_tasks != 0:
            user_complete_percent = round(((user_complete / user_tasks) * 100), 2)
            user_incomplete_percent = round(((user_incomplete / user_tasks) * 100), 2)
            user_overdue_percent = round(((user_overdue / user_tasks) * 100), 2)

        with open ("user_overview.txt", "a") as user_overview:
            user_overview.write(f"The task statistics for {users[user]['username']}:\n")
            user_overview.write("_____________________________________________\n")
            user_overview.write(f"The total number of tasks assigned to user: {user_tasks}\n")
            user_overview.write(f"The percentage of tasks assigned to user: {user_tasks_percent}%\n")
            user_overview.write(f"The percentage of tasks assigned to user that are completed: {user_complete_percent}%\n")
            user_overview.write(f"The percentage of tasks assigned to user that are incomplete: {user_incomplete_percent}%\n")
            user_overview.write(f"The percentage of tasks assigned to user that are overdue: {user_overdue_percent}%\n")
            user_overview.write("_____________________________________________\n")
            user_overview.write("\n")
        
    print("The requested reports have been generated.")
    print()

# Create admin_priviledge function for verifying admin rights.
def admin_priviledge():
    if username == "admin":
        admin_privilege = True
    else:
        admin_privilege = False
    return admin_privilege


# Login Section
# Handle login requests by calling the user_tracker function.
login()

# Display 2 different menu versions depending on whether
# user has admin privileges or not.
# Use while loop to manage menu navigation.
while True:
    admin = admin_priviledge()
    if admin == True:

        menu = input('''Select one of the following options below:
r - Register a user
a - Add a task
va - View all tasks
vm - View my tasks
d - Display statistics
g - Generate reports
e - Exit
: ''').lower()

    else:
        menu = input('''Select one of the following options below:
a - Add a task
va - View all tasks
vm - View my tasks
g - Generate reports
e - Exit
: ''').lower()

# This menu option is visible only to those with admin privileges.
# It allows them to register new users. Implement a check for
# admin rights to make sure only authorised users can use this.
    if menu == 'r':
        reg_user()
        
# This menu option is for assigning new tasks to users.
    elif menu == 'a':
        add_task()
        
# This menu option allows users to view all tasks.
    elif menu == 'va':
        view_all()
        
# With this menu option, we display only the tasks allocated to the current user.
    elif menu == 'vm':
        view_mine()
                    
# This is another menu option reserved for users with admin privileges.
# It gives a high level overview of users and tasks.
    elif menu == 'd':
        display_statistics()
        
    elif menu == 'g':
        generate_reports()
        
# Option to log out and exit menu.
    elif menu == 'e':
        print()
        print(f"Goodbye, {username}!!!")
        exit()

# Error message for invalid inputs.
    else:
        print("You have entered an invalid choice. Please try again!")
        print()