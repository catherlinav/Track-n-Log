#Define functions
def display_log():
    if len(activity_log) == 0:
        print('You currently have 0 tracked activities/hours.\n')
    else:
        print(f'You currently have {len(activity_log)} tracked activity(ies)\n')
        for activity in activity_log:
            print(f'{activity['activity']}: {activity['hours']} hours\n')

def edit_activities():
    option = input('Would you like to add or delete an activity (a/d)? ').lower()
    if option == 'a':
        add_choice = input('Enter name of activity you would like to add: ')
        new_log = {'activity': add_choice,
                   'hours': 0.0
                   }
        activity_log.append(new_log)
        print(f'\nSuccesfully added new activity: {add_choice}')
        return
    elif option == 'd':
        if len(activity_log) == 0:
            print('You don\'t have any activities to delete.\n')
            return
        else:
            print('List of available activities:')
            for activity in activity_log:
                print(f'\n{activity['activity']}: {activity['hours']} hours\n')
            
            delete_choice = input('Enter name of activity you would like to delete: ')
            for index, log in enumerate(activity_log):
                if log['activity'].lower() == delete_choice.lower():
                    activity_log.pop(index)
                    print(f'\nSuccessfully removed the activity: {delete_choice}')
                    return
                    
    else:
        print('Invalid option.\n')
        return

def track_hours():
    #Put all available acitivities in a list
    activity_list = []
    for activity in activity_log:
            activity_list.append((activity['activity']).lower())

    #Print the log of activities and their hours
    print('List of available activities:')
    for activity in activity_log:
        print(f'{activity['activity']}: {activity['hours']} hours\n')
    
    #Ask user for input
    choice = input('Enter choice of activity: ').lower()
    if choice not in activity_list:
        print('\nInvalid choice of activity.')
        return
    else:
        #Ask user for input
        hours_input = float(input('Enter the number of hours you\'d like to add: '))
        if not(hours_input > 0):
            print('\nInvalid number.')
            return
        else:
            #Add the hours to the activity choice
            for log in activity_log:
                if (log['activity']).lower() == choice:
                    log['hours'] += hours_input
            print(f'\nSuccessfully added {hours_input} to {choice}')
            return

#Display welcome message
activity_log = []
is_running = True
while is_running:
    print('-' * 52)
    print('\tWelcome to the Hour Tracker!')
    print('-' * 52)
    print('1. Display tracked hours')
    print('2. Edit activities')
    print('3. Track hours')
    print('4. Exit')
    print('-' * 52)
    choice = input('Choose an option (1-4): ')

    if choice == '1':
        display_log()
    elif choice == '2':
        edit_activities()
    elif choice == '3':
        if len(activity_log) == 0:
            print('\nThere are currently no logged activities. Please add in \'Edit Activities.\'')
            is_running = False
        else:
            track_hours()
    elif choice == '4':
        print('\nThank you! Have a nice day!')
        is_running = False
    else:
        print('\nInvalid choice.')
        is_running = False
