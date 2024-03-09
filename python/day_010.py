#fix the code
multiplicação = 3.4 * 6.8
divisão = 2467 / 4673
potência = 10 ** 2
resto = 343 % 100
divisão_inteira = 343 // 100

print(multiplicação)
print(divisão)
print(potência)
print(resto)
print(divisão_inteira)

#100 days of code: day 10
#Bill calculator
print("Welcome to the tip calculator.")
bill = float(input('What is the bill? '))
tip = int(input('What percentage tip would you like to give? '))
people = int(input('How many people to split the bill? '))
print()

whole_bill = bill + (bill * (tip / 100))
bill_per_person = whole_bill / people

print(f'Bill: $ {whole_bill:.2f}')
print (f'Each person should pay $ {bill_per_person:.2f}')





