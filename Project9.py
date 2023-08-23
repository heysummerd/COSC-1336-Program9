#---------------------
# Summer Davis
# COSC 1336
# Project 9
#---------------------
# Objective: collect acceleration/brake data to display a
# specific car's travel summary.
#
# Program will:

# Create a CarTravel class
# - CarTravel class will contain data members for:
# --> make, year, speed (0)
# - CarTravel class will have accessors for each data member
# - CarTravel class will have methods to accelerate/brake by 5mph

# Establish a car object to reference CarTravel class
# - ask user to enter car make and year (validate input)
# - ask user how many times they used accelerate/brake
# - display results using a for loop for each accelerate/brake

#---------------------

# class CarTravel will collect and apply car travel information
class CarTravel:

    def __init__(self, make, year):
        self.make = make
        self.year = year
        self.speed = 0

    def getMake(self):
        return self.make

    def getYear(self):
        return self.year

    def getSpeed(self):
        return self.speed

    def accelerate(self):
        self.speed += 5

    def brake(self):
        self.speed -= 5
        

# Collect and organize all of the program tasks
def main():
    
    # Header of the project
    header()

    # Collect make and year
    make = getStringData('Car Make: ')
    year = getIntegerData('Enter year: ')
    print('\n')

    # Create Car object
    car = CarTravel(make, year)

    # Get number of times car accelerates
    carAccelerate = getIntegerData('How many times did you accelerate? ')
    carBrake = getIntegerData('How many times did you brake? ')

    # Display car travel summary
    displayResult(car, carAccelerate, carBrake)
    
    # End of project display
    footer()

# Display car travel summary
def displayResult(car, carAccelerate, carBrake):
    print('\n')
    print('_' * 80)
    print('Car Travel Information')
    print('_' * 80)

    print('Acceleration applied:')
    print('-' * 20)

    count = 1
    for each in range(carAccelerate):
        car.accelerate()
        print(f'Accelerate #{count}:' + \
              f'\t\tIncrease by 5mph\t\t' + \
              f'Current speed: {car.getSpeed()} mph')
        count += 1

    print(f'\nBrake Applied')
    print('-' * 13)
    
    count = 1
    for each in range(carBrake):
        car.brake()
        print(f'Brake #{count}:' + \
              f'\t\tdecrease by 5mph\t\t' + \
              f'Current speed: {car.getSpeed()} mph')
        count += 1

    print('_' * 80)
    print(f'{car.getMake()} Final Speed:\t\t{car.getSpeed()} mph')
    print('-' * 60)
        
        

# Get users entry of string data
def getStringData(prompt):
    while (True):
        value = input(prompt)

        if (len(value) > 0):
            return value
        else:
            print('\n\tError: Please enter a make for the car.\n')

# Get users entry of ONLY integer data
def getIntegerData(prompt):
    while (True):
        try:
            value = int(input(prompt))
            return value

        except ValueError: 
            print(f'\n\tError: Non Integers entered.\n')

# Display the start of the project
def header ():
    print('\n')
    print('My Car Information')
    print('-' * 60)
    
# Display the end of the project
def footer():
    print('\n')
    print('-' * 60)
    print('End of Project 9')

# Call the main function  
main()
