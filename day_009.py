#100 days of code: day 9
print('GENERATION GENERATOR')
print()
print("Let's find out what generation you belong to:")
birth = int(input('When were you born? '))

if birth >= 1925 and birth <= 1946:
  print('You are a Tranditionalist')
elif birth >= 1947 and birth <= 1964:
  print('You are a Baby Boomer')
elif birth >= 1965 and birth <= 1981:
  print('You are a Generation X')
elif birth >= 1982 and birth <= 1995:
  print('You are a Millenial')
elif birth >= 1996 and birth <= 2015:
  print('You are a Generation Z')
else:
  if birth <= 1924 or birth >= 2016:
    print('You are either too old or too young to be on this list')
  else: 
    print('Something went wrong. Please try again later...')
    

