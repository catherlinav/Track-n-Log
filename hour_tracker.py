#Define functions
def display_log():
    if len(activity_log) == 0:
        print('You currently have 0 tracked activities/hours.\n')
    else:
        print(f'You currently have {len(activity_log)} tracked activity(ies)\n')
        for activity in activity_log:
            print(f'{activity['activity']}: {activity['hours']} hours\n')

def edit_activities():
    pass

def track_hours():
    activity_list = []
    valid = True
    while valid:
        for activity in activity_log:
            print(f'{activity['activity']}: {activity['hours']} hours\n')
        choice = input('Enter choice of activity: ').lower()

        for activity in activity_log:
            activity_list.append((activity['activity']).lower())

        if choice not in activity_list:
            print('Invalid choice of activity.')
            valid = False

        hours_input = int(input('Enter the number of hours you\'d like to add: '))
        if hours_input <= 0:
            print('Invalid number.')
            valid = False
        
        for activity in enumerate(activity_log):
            



#Display welcome message
activity_log = [
    {'activity' : 'Name',
     'hours' : 0}
    ]
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
        track_hours()
    elif choice == '4':
        print('\nThank you! Have a nice day!')
        is_running = False
    else:
        print('\nInvalid choice.')
        is_running = False
