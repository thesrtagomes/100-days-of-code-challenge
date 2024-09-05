# Day 30 -- Pamela Gomes
# Alignment = < left | > Right | ^ center

print('30 Days Down - What did you think?')
print()

for i in range(1,31):
    print(f'Day {i}:')
    user_input = input()
    response = f'You thought Day {i} was {user_input}'
    print(f'{response:^40}')
    print()