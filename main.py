from menu import*
from descriptiveStatistics import*

#This function processes all the options
def process_request(option):  
    #Descripive Statistics
    if(option == 1):
        descriptiveStatistics()
        

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

