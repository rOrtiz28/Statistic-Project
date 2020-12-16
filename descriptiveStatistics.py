from numpy.core.fromnumeric import sort
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
    except TypeError:
        return -1

def valid_ValT():
    vFlag = True
    while vFlag == True:
        valT = (input("Enter the percent that you want to trim (Eg. 10% will be '10'): "))
        valT_info = isFloat(valT)
        if valT_info != -1:
            vFlag = False
            return valT_info
        else:
            print("Invalid input, Please use a integer like the following: 10% will be 10")
            vFlag = True
    
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
                                #print(sorted(medianList))
                                print(np.median(medianList))
                if(option_info == 3):
                    done = True
                    trimmedDone = False
                    print("You're in Trimmed mode")
                    trimmedList = []
                    while trimmedDone != True:
                        trimmedInput = input("Enter the scores to get the Trimmed Mean (If you finish enter a key that is not equal to a number): ")
                        score_info = isFloat(trimmedInput)
                        if score_info != -1:
                            trimmedList.append(score_info)
                        elif score_info == -1:
                            trimmedDone = True
                            if len(trimmedList) <= 0:
                                print("The list is empty or you have invalid scores")
                                trimmedDone = False
                            else:          
                                print("Unsorted List:", trimmedList)
                                valid_TrimmedList = sorted(trimmedList)
                                print("Sorted List:", valid_TrimmedList)
                                valT_Valid = valid_ValT()
                                lenList = len(trimmedList)
                                valRemoved = lenList * (valT_Valid / 100)
                                finalValueToRemove = int(np.ceil(valRemoved))
                                print(finalValueToRemove)
                                if lenList >= (finalValueToRemove * 2):
                                    for i in range(finalValueToRemove):
                                        del valid_TrimmedList[0]
                                        del valid_TrimmedList[-1]
                                
                                    print(valid_TrimmedList)
                                    print(np.average(valid_TrimmedList))
                                else:
                                    print("The percent of values that you want to trim is more than the list number!")
                                    trimmedDone = False
                                    
                                    
                                    
                                