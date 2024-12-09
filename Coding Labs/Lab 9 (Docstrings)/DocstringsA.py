#----------------------------------------------------------------------
# Name:        #Docstrings A
# Purpose:     #Does John math
#
# Created:     5-Nov-2024
# Updated:     5-Nov-2024
#----------------------------------------------------------------------

#converts celsius to fahrenheit, rounds to 2 decimals
def celsius_to_fahrenheit(celsius):
    '''
    Converts inputted celsius to degress
  
    Parameters
    ----------
    celsius: float
        celsius inputted

    Returns
    -------
    float
        Calculated value of the corrosponding fahrenheit value
    '''
    return(round(celsius * 9/5 + 32, 2))

#miles to kms, rounds to 2 decimals
def miles_to_kilometers(miles):
    '''
    Converts inputted miles to km
  
    Parameters
    ----------
    miles: float
        miles inputted

    Returns
    -------
    float
        Calculated value of the corrosponding km value
    '''
    return(round(miles * 1.60934), 2)

#converts hours and minutes into just minutes
def time_to_minutes(hours, minutes):
    '''
    Converts inputted hours + minutes to minutes
  
    Parameters
    ----------
    hours: float
        hours inputted
        
    minutes: floast
        minutes inputted

    Returns
    -------
    float
        Calculated value of the corrosponding minutes value
    '''
    return(hours * 60 + minutes)

#runs all functions
celsius = float(input())
fahrenheit = celsius_to_fahrenheit(celsius)
print(f"{celsius}C is equal to {fahrenheit}F")

miles = float(input())
km = miles_to_kilometers(miles)
print(f"{miles} miles is equal to {km} kilometers")

hours = int(input())
minutes = int(input())
total_minutes = time_to_minutes(hours, minutes)
print(f"{hours} hours and {minutes} minutes is equal to {total_minutes} minutes")
