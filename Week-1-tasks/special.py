'''Implement the function check_year that reports if the given year is special. 
The function should return True or False.
Ex:  (20+25)^2=2025
'''
def check_year(year):
    year_str = str(year)

    x = int(year_str[0:2])
    y = int(year_str[2:])

    return (x+y)**2 == year 
    

if __name__ == "__main__":
    print(check_year(1995)) # False
    print(check_year(2024)) # False
    print(check_year(2025)) # True
    print(check_year(2026)) # False
    print(check_year(3025)) # True
    print(check_year(5555)) # False