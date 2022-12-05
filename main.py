import random

# A random number guessing script.
# Idea is from https://www.upgrad.com/blog/python-projects-ideas-topics-beginners/
user_input = input('guess the number 1-10 ')
number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
random_number = random.choice(number_list)

# Turns the int into string.
user_inputSTR = str(user_input)
random_numberSTR = str(random_number)

# Print if he's correct or not.
if user_inputSTR > random_numberSTR:
    print('close, just a bit lower. Good luck next time!')
elif user_inputSTR < random_numberSTR:
    print('close, just a bit higher. Good luck next time!')
else:
    print('correct!')


