# NA Gaitate 31711820

# Define main
def main():
    print('=============================')
    print('Music Festival Band Scheduler')
    print('=============================')
    display_menu()

    band_count = 0
    total_time = 0
    long_band = ''
    long_duration = 0
    max_bands = 5
    choice = 0

# Entering the loop to check conditions
    while choice != 4:
        choice = int(input('Enter your choice: '))

        if choice == 1:
            if band_count >= max_bands:
                print('Maximum number of bands reached.')
            else:
                band_name = input('Enter band name: ')
                duration = int(
                    input(f'Enter set duration (minutes) for {band_name}: '))
                duration = validate_duration(duration)

                band_count += 1
                total_time += duration

                if duration > long_duration:
                    long_duration = duration
                    long_band = band_name

        elif choice == 2:
            if band_count == 0:
                print('No bands added yet. Please add bands first (Option 1).')
            else:
                print('Total performance time:', total_time, 'minutes')

        elif choice == 3:
            if band_count == 0:
                print('No bands added yet. Please add bands first (Option 1).')
            else:
                print('Band with the longest set:',
                      long_band, f'({long_duration} minutes)')

        elif choice == 4:
            print('Exiting the program')

        else:
            print('Invalid option. Please choose between 1 and 4.')

        if choice != 4:
            print()
            display_menu()


# Validating function
def validate_duration(duration):
    while duration <= 0:
        print('Duration must be a positive number.')
        duration = int(input('Enter set duration in minutes: '))
    return duration


# menu displaying function
def display_menu():
    print('Menu:')
    print('1. Add band performance')
    print('2. Show total performance time')
    print('3. Show band with longest set')
    print('4. Exit the program')


# Call main function
main()
