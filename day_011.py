# 100 days of code: day 11
print('Time converter')
print()
print('Do you wanna know How many seconds are in a year?')
type_of_year = input('Is it a leap year? yes/no: ').lower()

seconds_in_minutes = 60
seconds_in_hour = seconds_in_minutes * 60
seconds_in_day = seconds_in_hour * 24

if type_of_year == 'yes' or type_of_year == 'y':
  seconds_in_year = seconds_in_day * 366
  
elif type_of_year == 'no' or type_of_year == 'n':
  seconds_in_year = seconds_in_day * 365
  
else:
  print('Error.Please try again.')
  exit()
  
print(f'There are {seconds_in_year} seconds in a year')

