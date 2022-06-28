def new_game():
    user_answer = []
    correct_guess = 0
    question_num = 1
    for key in questions:
        print('#-----------------------------------------#')
        print(key)
        for i in options[question_num-1]:
            print(i)
        a = input("Answer: ").upper()
        user_answer.append(a)
        correct_guess += check_answer(questions.get(key), a)
        question_num += 1

    display_score(correct_guess,user_answer)

def check_answer(answer, guess):
    if answer == guess:
        print("Correct!")
        return 1
    else:
        print("Wrong!")
        return 0

def display_score(correct_guess, user_answer):
    print('--------------------------')
    print("Results")
    print('--------')
    print('Answer:', end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print('\nUser Answer:', end="")
    for i in user_answer:
        print(i, end=" ")

    score = (correct_guess/len(questions))*100
    print('\nCorrect Answer: '+str(score))

def play_again():
    check = input('Do you answer again:(y/n):')
    if(check == 'y'):
        return True
    if(check == 'n'):
        return False


questions = {'The national bird is:': 'A',
             'The national fruit is:': 'D',
             'The national religion is:': 'A'}

options = [['A. Doel', 'B. Parrot', 'C. Dove', 'D. Pigeon'],
           ['A. Banana', 'B. Mango', 'C. Apple', 'D. Jackfruit'],
           ['A. Islam','B. Hindu','C. Buddist','D. Christan']]

new_game()

while play_again():
    new_game()
