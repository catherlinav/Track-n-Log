
import sqlite3
import pandas as pd

conn = sqlite3.connect('activities.db') # set up to database
c = conn.cursor() # create cursor


# create table for the activities
c.execute("""CREATE TABLE IF NOT EXISTS activities_log 
          (
          id INTEGER PRIMARY KEY,
          Title TEXT,
          Hours INT              
          )""")

def is_table_empty(): # checks if table is empty
    c.execute("SELECT COUNT(*) FROM activities_log")
    count = (c.fetchone())[0] # it returns a tuple, so we need to get first value
    return (count == 0) # returns True or False

def display_log(): # show the activities log
    if is_table_empty(): # displays msg if table is empty
        print('You currently have 0 tracked activities/hours.')
    else:
        query = ("SELECT * FROM activities_log")
        df = pd.read_sql_query(query, conn) # display SQL query with pandas
        print(df)

def add_activity(act): # add an activity ('hours' set to 0)
    with conn:
        c.execute("INSERT INTO activities_log (Title, Hours) VALUES (:title, 0)",
                  {'title': act})
    print(f'{act} has been added to your Track n Log!')

def remove_activity(act): # remove an activity
    with conn:
        c.execute("DELETE FROM activities_log WHERE Title = :title",
                  {'title': act})
    print(f'{act} has been removed from your Track n Log!')

def add_hours(act, hours): # add hours to existing activity
    with conn:
        c.execute("""UPDATE activities_log SET Hours = Hours + :hours
                  WHERE Title = :title""",
                  {'hours': hours, 'title': act})
    print(f'Successfully added {hours} hour(s) to {act}!')


# main code
# Welcome messages

while True:
    print('-' * 52)
    print('\tWelcome to Track n Log!')
    print('-' * 52)
    print('1. Display activity log')
    print('2. Edit activity log')
    print('3. Track hours')
    print('4. Exit')
    print('-' * 52)
    choice = input('Choose an option (1-4): ')

    if choice == '1':
        display_log()
    elif choice == '2':
        option = input('Would you like to add or remove an activity (A/R)? ').upper().strip()
        if option == 'A':
            act = input('Enter name of activity you\'d like to add: ').upper().strip()
            add_activity(act)
        elif option == 'R':
            if not is_table_empty():
                display_log()
                act = input('Enter name of activity you\'d like to remove: ').upper().strip()
                remove_activity(act)
            else:
                print('There is nothing to remove!')
        else:
            print('Invalid option!')
    elif choice == '3':
        if is_table_empty(): # displays msg if table is empty
            print('\nThere are currently no logged activities. Please add in \'Edit activity log.\'\n')
        else:
            display_log() # show available options
            act = input('Enter choice of activity: ').upper().strip() 
            hours = input('Enter the number of hours you\'d like to add: ')
            # checks if 'hours' input is a number
            if hours.isdigit():
                hours = int(hours)
                    # checks if 'hours' input is valid
                if hours > 0:
                    add_hours(act, hours)
                else:
                    print('Number of hours must be greater than 0!')
            else:
                print('Input must be a number!')
           
    elif choice == '4':
        print('\nThank you! Have a nice day!')
        break
    else:
        print('Invalid choice.')


conn.close() # close connection

