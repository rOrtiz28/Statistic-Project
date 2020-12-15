#This function prints the initial menu
def print_program_menu():
    print("\n")
    print("Welcome to the probability & statistics calculator. Please, choose an option:")
    print("1. Descripive Statistics")
    #print("2. ")
    #print("3. ")
    #print("4. ")
    #print("5. ")
    print("6. Exit")

#Checks if option is a number
def identify_option(option):
    if option.isdigit() :  # Verify if this is a number
        numeric_option = int(option)
        # check if in range
        if numeric_option >= 1 and numeric_option <= 6:
            return numeric_option
        else:
            return -1 # invalid option
    else:
        return -1 # invalid option
    