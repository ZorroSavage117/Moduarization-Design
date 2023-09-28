# 1. Name:
#      Arlo Jolley
# 2. Assignment Name:
#      Lab 03 : Calendar Program
# 3. Assignment Description:
#      It caculates what the month looks like for a sertain year
# 4. What was the hardest part? Be as specific as possible.
#      The hardest part was get the Week start function because we couldent use sertain items that would have made it easier to do it
#      so I spent roughly 4 hours on it last week to get it out of the way.
# 5. How long did it take for you to complete the assignment?
#      it took me 7 hours to code this assignment
#  video link https://www.youtube.com/watch?v=NBqfH_xvlHU



def display_table(dow, num_days):
    '''Display a calendar table'''
    assert(type(num_days) == type(dow) == type(0))
    assert(0 <= dow <= 6)
    assert(28 <= num_days <= 31)

    # Display a nice table header
    print("  Su  Mo  Tu  We  Th  Fr  Sa")

    # Indent for the first day of the week
    for indent in range(dow):
        print("    ", end='')

    # Display the days of the month
    for dom in range(1, num_days + 1):
        print(repr(dom).rjust(4), end='')
        dow += 1
        # Newline after Saturdays
        if dow % 7 == 0:
            print("") # newline

    # We must end with a newline
    if dow % 7 != 0:
        print("") # newline

def week_start(year, month):
    if month == 1 or month == 2:
        month += 12
        year -= 1
   
    k = 1  
    m = month
    D = year % 100
    C = year // 100
    
    f = k + ((13 * (m + 1)) // 5) + D + (D // 4) + (C // 4) - 2 * C
    
    day_start = (f % 7 - 1) % 7
    
    return day_start

def month_days(month, leap):
    if month == 2:
        if leap:
            return 29
        else:
            return 28
    elif month == 4 or month == 6 or month == 9 or month == 11:
        return 30
    else:
        return 31

def is_leap_year(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 == 0:
        return True
    else:
        return False

def get_month():
    no_error = True
    while no_error:
        try:
            month = int(input("Please enter a mounth: "))
        except ValueError:
            print("Month must be an integer.")

        if month > 0 and month < 13:
            return month
        else:
            print("Month must be between 1 and 12.")
        
def get_year():
    no_error = True
    while no_error:
        year = int(input("Please enter a year: "))
        if year >= 1753:
            return year
        else:
            print("Year must be 1753 or later.")

# Output
# display_table(0, 31)
def main():
    month = get_month()
    year = get_year()
    print()
    display_table(week_start(year, month), month_days(month, is_leap_year(year)))
    print()
    again = int(input("Run again?(1/0): "))
    if again == 1:
        main()

if __name__ == "__main__":
    main()