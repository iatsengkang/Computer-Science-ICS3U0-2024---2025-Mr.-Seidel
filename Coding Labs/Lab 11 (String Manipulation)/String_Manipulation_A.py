#----------------------------------------------------------------------
# Name:        #String Manipulation A
# Purpose:     #Does John math
#
# Created:     12-Nov-2024
# Updated:     12-Nov-2024
#----------------------------------------------------------------------

#variable that makes sure that the program keeps running until a valid input is ran
Validity = True
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
        
    Raises
    ------
    TypeError
        If temperature is not an int or float
    Exception
        If the Fahrenheit calculation goes awry
    '''
    if not isinstance(celsius, (int, float)):
        raise TypeError("input was expected to be int or float")
    return(round(float(celsius) * 9/5 + 32, 2))

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
                
    Raises
    ------
    TypeError
        If miles is not an int or float
    Exception
        If the miles to km conversion calculation goes awry
    '''
    if not isinstance(miles, (int, float)):
        raise TypeError("input was expected to be int or float")
    if miles < 0:
        raise ValueError("input was expected to be a positive number")
    return(round(float(miles) * 1.60934, 2))

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
                    
    Raises
    ------
    TypeError
        If hours and minutes is not an int or float
    Exception
        If the minutes conversion calculation goes awry
    '''
    if not isinstance(minutes, (int, float)) and not isinstance(hours, (int, float)):
        raise TypeError("inputs expected to be both a int or float")
    if hours < 0 or minutes < 0:
        raise ValueError("inputs expected to be both larger than zero")
    return(float(hours) * 60 + float(minutes))

#runs all functions, returns error messages if the input was invalid and tries again
while Validity == True:
    celsius = input()
    celsius = celsius.replace(" ", "")
    try:
        fahrenheit = celsius_to_fahrenheit(float(celsius))
        print(f"{celsius}C is equal to {fahrenheit}F")
        Validity = False
    except (ValueError, TypeError):
        print("Input must be a positive number, please try again")
        continue
    except Exception as e:
        print(f"Unexpected Error: {e}")
        break

Validity = True
while Validity == True:
    miles = input()
    miles = miles.replace(" ", "")
    try:
        km = miles_to_kilometers(float(miles))
        print(f"{miles} miles is equal to {km} kilometers")
        Validity = False
    except (ValueError, TypeError): 
        print("Values must be whole numbers, please try again")
        continue 
    except Exception as e:
        print(f"Unexpected Error: {e}")

Validity = True
while Validity == True:
    hours = input()
    minutes = input()
    hours = hours.replace(" ", "")
    miniutes = minutes.replace(" ", "")
    try:
        total_minutes = time_to_minutes(float(hours), float(minutes))
        print(f"{hours} hours and {minutes} minutes is equal to {total_minutes} minutes")
    except (ValueError, TypeError):
        print("Values must be both whole numbers")
        continue
    except Exception as e:
        print(f"Unexpected Error: {e}")