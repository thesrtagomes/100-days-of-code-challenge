# 100 days of code: day 8
print('Welcome to the Mood Tracker Machine!')
print()
name = input('What is your name? ')
day_of_the_week =  input('What day of the week is today? ').lower()
mood = int(input('in a scale of 1 to 10, how are you feeling today? '))

if day_of_the_week == "monday" or day_of_the_week.lower() == "tuesday" or day_of_the_week.lower() == "wednesday" or day_of_the_week.lower() == "thursday" or day_of_the_week.lower() == "friday":
           
  if mood > 0 and mood <= 5:
    print('Hey', name, 'I know it is still', day_of_the_week.title(), 'and I know you are feeling a bit down. I feel you are going to have a great day. Trust me!')
  elif mood > 5 and mood <= 10:
    print(' Hi', name, '. I am happy to hear that you feel ', mood, ' in a scale of 1 to 10. Today is a beautiful ', day_of_the_week,'. You deserve great days!')
  else:
    print('I am sorry. Please select a valid number to measure our scale.')
    
elif day_of_the_week == 'saturday' or day_of_the_week.lower() == 'sunday':
  
  if mood > 0 and mood <= 5:
    print('Oh no ', name, '! I know it is ', day_of_the_week.title(), '. It is totally normal to feel this way. I hope the next weekend will be better than this one. I know you deserve to take a good rest!')
  elif mood > 5 and mood <= 10:
    print('Uhull! It is a great opportunity to enjoy your weekend. I hope you have a great day, ', name, '!')
  else:
    print('I am sorry. Please select a valid number to measure our scale.')
    
else: 
  print('I am sorry. Please select a valid day of the week.')
  
    
    
    
          