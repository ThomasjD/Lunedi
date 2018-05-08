#To do list app
#User should be able to add task by adding the title of the task 
# User should be able to view all the tasks 
# User should be able to remove the tasks 
# User should be able to quit the app when "q" is pressed 

#HARD MODE: 
# User should be able to enter priority of the task 
# User should be able to sort the tasks based on priority 

import sys

tasks = []

def now_what():
    print("What do you want to do now?")
    print("Press (m) for menu or (q) to quit")
    option = input()
    if option == 'm':
        menu()
    else:
        sys.exit()

def menu():    
    print("Press [v] to view tasks. ")
    print("Press [a] to add task. ")
    print("Press [d] to delete task. ")
    print("Press [q] to quit. ")
    option = input('What would you like to do?').lower()
    if option == 'v':
        task_list()
        now_what()
    elif option == 'a':
        add_task()
    elif option == 'd':
        delete_task()
    else: 
        sys.exit()


def add_task():    
    
    add_more = True
    while (add_more == True):
        print ("Enter the task")
        task = tasks.append(input())
        #task = input("Enter your task. ")
        task_list()
        option2 = input("Do you want to add more tasks? (y/n)")
        if option2 == "y":
            continue
        else:
            add_more = False
    now_what()

def delete_task():
    delete_more = True
    while (delete_more == True):
        task_list()
        print ("Enter the task # that you want to delete")
        option = int(input())-1
        del tasks[option]
        task_list()
        option2 = input("Do you want to delete more tasks? (y/n)")
        if option2 == "y":
            continue
        else:
            delete_more = False
    now_what()

def task_list(): 
    if len(tasks) == 0:
        print("You dont have anything in your task list")
        now_what()
    else: 
        count = 1
        for x in tasks:
            print (f'{count}. {x}')
            count += 1

menu()



