
dummy = "DUMMY"
#This function prints the menu
def print_program_menu():
    print("\n")
    print("Welcome to the probability & statistics calculator. Please, choose an option:")
    print("1. ")
    print("2. ")
    print("3. ")
    print("4. ")
    print("5. ")
    print("6. Exit")
    
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

#This function processes all the options
def process_request(option):
    print("Dummy")


def main():
    done = False
    while not done:
        print_program_menu()
        user_option = input("Enter option: ")
        option_info = identify_option(user_option)
        if option_info != -1:
            #option was valid
            if option_info == 6:
                done = True
                print( "Thanks for using the probability & statistics calculation program")
            else:
                process_request(option_info)
        else:
            #option invalid
            print("Invalid Option\n")
            
if __name__ == "__main__":
    main()

