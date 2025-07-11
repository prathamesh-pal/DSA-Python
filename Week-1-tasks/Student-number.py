'''A University of Helsinki student number is a sequence of nine digits. The first digit is 0 and the 
    last digit is a check value that allows checking for typos in the student number.
The check value is obtained by summing up the other digits multiplied by 
the values 3,7,1,3,7,1,3,7 in the left-to-right order. If the sum is a multiple of 10, the check digit is 0. 
Otherwise, the check digit is the distance of the sum to the next multiple of 10.'''

# Example :
''' For example, if the student number is 012749139, 
the sum is 3.0 + 7.1 + 1.2 + 3.7 + 7.4 + 1.9 + 3.1 + 7.3 = 91. 
 The next multiple of 10 is 100 and the distance to that is 9. 
 Thus the last digit of the student number is 9.'''


def check_number(number):
    if len(number) != 9 or not number.isdigit() or number[0] != '0':
        return False

    Check_Value = [3,7,1,3,7,1,3,7]
    sum_of_Number = 0
    for num in range(len(Check_Value)):

        sum_of_Number  +=  int(number[num])*Check_Value[num] 

    check_digit = (10 - (sum_of_Number % 10)) % 10 
    last_digit = int(number[-1])
    return check_digit == last_digit 


if __name__ == "__main__":
    print(check_number("012749138")) # False
    print(check_number("012749139")) # True
    print(check_number("013333337")) # True
    print(check_number("012345678")) # False
    print(check_number("012344550")) # True
    print(check_number("1337"))      # False
    print(check_number("0127491390")) # False
