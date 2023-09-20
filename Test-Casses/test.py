def start_of_the_week(year, month):
    # Adjust month and year for January and February
    if month in (1, 2):
        month += 12
        year -= 1
    
    # Calculate the day of the week using Zeller's Congruence
    k = 1  # Day of the month is always 1
    m = month
    D = year % 100
    C = year // 100
    
    f = k + ((13 * (m + 1)) // 5) + D + (D // 4) + (C // 4) - 2 * C
    
    # Adjust the result to represent Sunday as 0
    day_of_week = (f % 7 - 1) % 7
    
    return day_of_week

# Example usage:
year = 2023
month = 1
result = start_of_the_week(year, month)
print(f"The 1st day of {month}/{year} is a Sunday (0-based index): {result}")
