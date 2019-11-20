from logins import *

#Functions to check inputted parameters

#Check the input value of the Lower Rate Limit to match the range requirements and return True if valid
def checkLRL(value):
    if value >=30 and value <=175:
        return True
    else:
        return False

#Check the input value of the Upper Rate Limit to match the range requirements and return True if valid
def checkURL(value):
    if value >=50 and value <=175:
        return True
    else:
        return False

#Check the input value of the Atrial/Ventricular Amplitude to match the range requirements and return True if valid
def checkAmp(value):
    if (value >=0.5 and value <=3.2) or (value >=3.5 and value <=7.0) or (value==0):
        return True
    else:
        return False

#Check the input value of the Atrial/Ventricular Pulse Width to match the range requirements and return True if valid
def checkPW(value):
    if (value >=0.1 and value <=1.9) or (value == 0.05):
        return True
    else:
        return False

#Check the input value of the Atrial/Ventricular Refractory Period to match the range requirements and return True if valid
def checkRP(value):
    if value >=150 and value <=500:
        return True
    else:
        return False

#Check the input value of the Maximum Sensor Rate to match the range requirements and return True if valid
def checkMSR(value):
    if value >=50 and value <=175:
        return True
    else:
        return False

#Check the input value of the Fixed AV Delay to match the range requirements and return True if valid
def checkFAVD(value):
    if value >=70 and value <=300:
        return True
    else:
        return False

#Check the input value of the Activity Threshold to match the range requirements and return True if valid
def checkAT(value):
    if value == "V-Low" or value == "Low" or value == "Med-Low" or value == "Med" or value == "Med-High" or value == "High" or value == "V-High":
        return True
    else:
        return False

#Check the input value of the Reaction Time to match the range requirements and return True if valid
def checkReactTime(value):
    if value >=10 and value <=50:
        return True
    else:
        return False

#Check the input value of the Response Factor to match the range requirements and return True if valid
def checkRF(value):
    if value >=1 and value <=16:
        return True
    else:
        return False

#Check the input value of the Recovery Time to match the range requirements and return True if valid
def checkRecoveryTime(value):
    if value >=2 and value <=16:
        return True
    else:
        return False
