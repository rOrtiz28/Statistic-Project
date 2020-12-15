from menu import identify_option
import numpy as np
import re

def valid(option):
    
    finder_Letter = re.findall("[a-z]", option)
    
    
    if finder_Letter:
        return -1
    else:
        return False
    

def isFloat(option):
    if valid(option) != -1:
        try: 
            data = float(option)
            if type(data) is float:
                return data
            else:
                return -1
        except ValueError:
            return -1
    else:
        try: 
            return -1
        except RuntimeWarning:
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
                    sumScores = 0
                    
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
                    
                         
                    
            
            
        