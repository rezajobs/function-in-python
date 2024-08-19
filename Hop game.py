def hop(number):
    if number % 5 == 0:
        print(f'{number} is divisible by 5. hop!')
        return True
    else:
        print(f'{number} is not divisible by 5. Try again!')
    return False

while True:
    user_input = input('Enter any number (or type "exit" to quit): ')
    
    if user_input.lower() == 'exit':
        print("Exiting the program. Goodbye!")
        break
    
    try:
        number = int(user_input)
    except ValueError:
        print("That's not a valid number! Please enter an integer.")
        continue
    
    if hop(number):
        break
