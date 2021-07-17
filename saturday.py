import sys
import datetime
#
# Author : Vinaya Godina
# Email : vinaya.g35@gmail.com
#

def getAllfourthSaturdays(startdate, enddate):
    start = datetime.datetime.strptime(startdate, "%Y%m%d")
    end = datetime.datetime.strptime(enddate, "%Y%m%d")
    date_generated = [start + datetime.timedelta(days=x) for x in range(0, (end-start).days)]
    saturdays_date = {}
    saturday = []
    for date in date_generated:
        key = str(date.month)+"-"+str(date.year)
        if key not in  saturdays_date:                 
            firstday=datetime.date(date.year,date.month,1)    # first day of month
            first_w=firstday.isoweekday() # weekday of 1st day of the month
            if first_w == 7: # making sunday into 0
                first_w = 0
            fourthSaturday=28-first_w # subtracting first day of week with 28 to get fourth saturday
            fourthSaturdayDate = datetime.date(date.year,date.month,fourthSaturday)
            saturdays_date[key] = fourthSaturdayDate.strftime("%Y%m%d")
       
        fourthSaturday = int(saturdays_date[key][6:])
        if ((date.day % 5 == 0 and date.isoweekday() == 6 and date.day != fourthSaturday) or 
            (date.day % 5 != 0 and date.isoweekday() == 6 and date.day == fourthSaturday)) :
            saturday.append(date.strftime("%Y%m%d"))

    return saturday


print("Find 4th Saturday or Saturday whose day is multiple of 5")
print("@Author: Vinaya.g35@gmail.com")
print("Press Enter after giving input")
print("Enter the start date in YYYYMMDD format: ")
startdate = str(input())
print("Enter the end date in YYYYMMDD format:")
enddate= str(input())

print("List of Saturdays: ")
# Check the format

try:
    print(getAllfourthSaturdays(startdate,enddate))
except Exception as e:
    print(e)
     
