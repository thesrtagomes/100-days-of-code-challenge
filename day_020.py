#List generator: day 20/100
#Pamela Gomes
print("List generator")
starting_number = int(input('Start at: '))
ending_number = int(input('End before: '))
increment= int(input('Increment between values:'))

for i in range(starting_number, ending_number, increment):
    print(i)
