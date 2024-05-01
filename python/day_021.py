#day 21/100: math game
#Pamela Gomes
import random
print('Math Game!')
print()
print('How well do you know your math facts? ' 
      'Pick a number and I will give you 10 math facts')
user_number = int(input('Please, choose a number: '))
print()

good_words = ['Great work!', 'Awesome!', 'Keep going!', 'You can do it!']
correct_answer = 0
for i in range(1,11):
    answer = int(input(f'{i} x {user_number} = '))
    right_answer = user_number * i
    if answer == right_answer:
        print(random.choice(good_words))
        correct_answer += 1
    else:
        print(f'Nope. The right answer is {right_answer}. ')
if correct_answer == 10:
    print(f'You scored {correct_answer} out of 10.🚀⭐🔢 Congratulations! 🎉🎉🎉')
else:
    print(f'You scored {correct_answer} out of 10.')



  