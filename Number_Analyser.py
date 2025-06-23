# NA Gaitate
# Number analysis program

def main():
    list1 = []
    # Input(takes user input and analyse it)
    # Accepting a series of 20 numbers from the user

    for i in range(1, 21):
        validInput = False
        while not validInput:
            userInput = input(f'Enter value number {i}: ')
            # Processing(validating user input)
            # Prompts the user until the correct values are entered
            if userInput.isdigit():
                list1.append(int(userInput))
                validInput = True
            else:
                print('Please enter only numbers')
    print()
    # Output(Calling other functions to main function
    # And printing the results)
    lowest_number = determineLowest(list1)
    print('The lowest number in the list is:', lowest_number)
    highest_number = determineHighest(list1)
    print('The highest number in the list is:', highest_number)
    total_number = determineTotal(list1)
    print('The total of the numbers in the list is:', total_number)
    average = determineAverage(list1)
    print(f'The average of the numbers in the list is: {average: .2f}')


def determineLowest(list1):
    # Defining a function to calculate
    # Lowest number in the list
    lowest = list1[0]
    for num in list1:
        if num < lowest:
            lowest = num
    return lowest


def determineHighest(list1):
    # Defining a function to calculate
    # Highest number in the list
    highest = list1[0]
    for num in list1:
        if num > highest:
            highest = num
    return highest


def determineTotal(list1):
    # Defining a function to calculate
    # The total number in the list
    total = sum(list1)
    return total


def determineAverage(list1):
    # Defining a function to calculate
    # Average number in the list
    total = determineTotal(list1)
    average = total / len(list1)
    return average

    # Calling main function
if __name__ == '__main__':
    main()
