def is_leap(year):
    leap = False
    
    # Write your logic here
    if year == 2100:
        leap = False
    elif year % 4 == 0:
        leap = True
    else:
        leap = False
        
    return leap

year = int(input())
print(is_leap(year))