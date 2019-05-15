year=int(input("enter the yr:"))
if(year%4==0 and year%100!=0 or year%400==0):
print("it is a leap yr")
else:
print("its not a leap yr")
