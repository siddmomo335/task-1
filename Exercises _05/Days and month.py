#dictionary that maps month numbers to number of days
month_days = {
    1: 31,    #january
    2: 28,     #february
    3: 31,      #march
    4: 30,      #april
    5: 31,     #may
    6: 30,      #june
    7: 31,      #july
    8: 31,      #august
    9: 30,     #september
    10: 31,     #october
    11: 30,       #november
    12: 31,       #december
}
#ask the user to enter the month number 
month = int(input("enter the month number (1-12): "))

#check if the month number is valid
if month in month_days:
    #special case for february (leap year check)
    if month == 2 :
        leap_year = input("is it a leap year? (yes/no): ").lower()
        if leap_year == "yes":
            print("february has 29 days")
        else:
            print("february has 28 days")
             #for all other months
    else:
        print(f"this month has {month_days[month]} days.")
        #if the month number is not valid
else:
    print("invalid month number. please enter a number between 1 and 12.")
