#100 days of code: day 13
print('GRADE GENERATOR')
print()
testName = input('What is the name of the test? ')
maxScore = int(input('What is the maximum score you could receive? '))
yourScore = int(input('What is the score you received? '))
print()
numberScore = float(yourScore / maxScore)
percentageScore = (numberScore * 100)
percentageScore = round(percentageScore, 2)

if percentageScore >= 90 and percentageScore <= 100:
  print('You got', percentageScore, '%, which is an A+')
elif percentageScore >= 80 and percentageScore <= 89:
  print('You got', percentageScore, '%, which is an A')
elif percentageScore >= 70 and percentageScore <= 79:
  print('You got', percentageScore, '%, which is a B')
elif percentageScore >= 60 and percentageScore <= 69:
  print('You got', percentageScore, '%, which is a C')
elif percentageScore >= 50 and percentageScore <= 59:
  print('You got', percentageScore, '%, which is a D')
elif percentageScore <= 49:
  print('You got', percentageScore, '%, which is a U')
else:
  print('Error. Please try again')
  
