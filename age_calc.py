"""
This is an Age calculator game by me Abdulrahmn69
"""
import datetime

again = "y"
while again == "y":
    year = int(input("Enter ur birth year:\n"))
    month = int(input("Enter ur birth month:\n"))
    day = int(input("Enter ur birth day:\n"))
    
    t_days = (datetime.datetime.now() - datetime.datetime(year,month,day)).days
    t_years = (datetime.datetime.now() - datetime.datetime(year,month,day)).days / 365
    
    print("U have borned in {} leaved for {:d} days it's mean that ur age is {:.2f} year".format(datetime.datetime(year,month,day).strftime("%A"), t_days,t_years ))
    
    again = input("Another age ? y / n: \n").strip().lower()
    
else:
    print("Thanks for using our age calculator")