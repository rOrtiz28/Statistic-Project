from menu import identify_option
import numpy as np

def isFloat(option):
    try: 
        data = float(option)
        if type(data) is float:
            return data
        else:
            return -1
    except ValueError:
        return -1
  
#Descripive Statistics
def descriptiveStatistics():
    done = False
    while done != True:
        print("\nDescripive Statistics:")
        print("1. Medidas de Tendencia Central" , "\n2. Medidas de Dispersion")
        option = input("Enter option:")
        option_info = identify_option(option)
        
        if(option_info == 1):
            done = True
            deepDone = False
            
            while deepDone != True:
                print("1. Average")
                print("2. Median")
                print("3. Trimmed Mean")
                print("4. Mode")
                print("5. Go back")
                option = input("Enter option:")
                option_info = identify_option(option)
                
                if(option_info == 1):
                    deepDone = True
                    avgDone = False
                    print("You're in DeepDone") 
                    avgList = []
                    
                    while avgDone != True:
                        avgInput = input("Enter the scores to get the average (If you finish enter a key that is not equal to a number): ")
                        score_info = isFloat(avgInput)
                        if score_info != -1:
                            avgList.append(score_info)
                        elif score_info == -1:
                            avgDone = True
                            if len(avgList) <= 0:
                                print("The list is empty or you have invalid scores")
                                avgDone = False
                            else:
                                print(avgList)
                                print(np.average(avgList))
                if(option_info == 2):
                    done = True
                    medianDone = False
                    print("You're in the median")
                    medianList = []
                    while medianDone != True:
                        medianInput = input("Enter the scores to get the median (If you finish enter a key that is not equal to a number): ")
                        score_info = isFloat(medianInput)
                        if score_info != -1:
                            medianList.append(score_info)
                        elif score_info == -1:
                            medianDone = True
                            if len(medianList) <= 0:
                                print("The list is empty or you have invalid scores")
                                medianDone = False
                            else:
                                print(medianList)
                                print(np.median(medianList))
                if(option_info == 3):
                    done = True
                    trimmedDone = False
                    print("You're in Trimmed mode")
                    trimmedList = []
                    while trimmedDone != True:
                        trimmedInput = input("Enter the scores to get the median (If you finish enter a key that is not equal to a number): ")
                        score_info = isFloat(trimmedInput)
                        if score_info != -1:
                            trimmedList.append(score_info)
                        elif score_info == -1:
                            medianDone = True
                            if len(trimmedList) <= 0:
                                print("The list is empty or you have invalid scores")
                                trimmedDone = False
                            else:
                                print(trimmedList)
                                #print(np.(trimmedList))
                    
                    
                    
                    
                    
                         
                    
            
            
        