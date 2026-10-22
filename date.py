#Author: Owethu Kgatitsoe



def is_leap_year(year):
    

    """
    Checks if a given year is a loop year
    Returns True if leap year, False if its not
    """
    #Checks if its a loop year or not
    if year % 100 == 0 :
        return True
    elif year % 4 == 0:
        return True
    else:
        return False


def get_day_of_the_week(month, day, year):
    
    """
    This will calculate the day of the week for a given date according to these Steps:
    - Use last two digits of the year, 
    - Divide by 12 and take remainder,
    - Count how many 4s fit in the remainder, 
    - Add the day of the month
    - Add the month code
    - Apply leap year and century offsets, 
    - Take modulo 7 to get day_code and Map day_code to actual day name.
    """
    #Step 1 till step 4:
    last_two = year % 100
    twelves = last_two // 12
    remainder = last_two - (twelves * 12)
    fours = remainder // 4
    total = twelves + remainder + fours + day 

    #step 5: Calculating the month code:
    if month == 1:
        total += 1
    elif month ==2:
        total += 4
    elif month == 3:
        total += 4
    elif month == 4:
        total += 0
    elif month == 5:
        total += 2
    elif month == 6:
        total += 5
    elif month == 7:
        total += 0
    elif month == 8:
        total += 3
    elif month == 9:
        total += 6
    elif month == 10:
        total += 1
    elif month == 11:
        total += 4
    elif month == 12:
        total += 6

    #step 6 The leap year and centuary of sets:
    if is_leap_year(year):
        if month == 1 or month == 2:
            total += 6

    if 1600 <=year < 1700:
        total += 6
    elif 1700 <= year < 1800:
        total += 4
    elif 1800 <= year < 1900:
        total += 2
    elif 2000 <= year < 2100:
        total += 6
    elif 2100 <= year < 2200:
        total += 4

    #step 7 modulus 7 for the day code:
    day_code = total % 7

    #step 8 mapping of the day_code to the days name
    if day_code == 0:
        return "Saturday"
    elif day_code == 1 :
        return "Sunday"
    elif day_code == 2:
        return "Monday"
    elif day_code == 3:
        return "Tuesday"
    elif day_code == 4:
        return "Wednessday"
    elif day_code == 5:
        return "Thursday"
    elif day_code == 6:
        return "Friday"



def main():
    """
    Running tests to check if the function actually works
    """
    print(get_day_of_the_week(12,25,2022))
    print(get_day_of_the_week(8,26,2022))
    print(get_day_of_the_week(10,5,1972))
    print(get_day_of_the_week(2,3,2016))
    print(get_day_of_the_week(12,18,1899))

main()
