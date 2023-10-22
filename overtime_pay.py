#hours work


#input
hours = float(input('enter number of hours worked'))
rate = float(input('enter hourly rate'))

#process
pay = float(rate)
hours_w =float(hours)
overt_rate = 27.69
if(hours <= 80):
    pay = hours * pay
else:
    pay = (80 * pay) + (hours - 80) * 27.69

#output  
print('hours worked',hours)
print('pay',pay)
if (pay <= 1476.82):
    print('no overtime')
else:
    print('overtime') 

