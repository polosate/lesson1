answers = {
    'привет': 'И тебе привет!',
    'как дела': 'Лучше всех!',
    'пока': 'Увидимся!'
}

def get_answers(question, answers):
    question = question.lower().strip()
    for char in question:
        if char in "?.!/;:":
            question = question.replace(char, '')
    default_answer = "Сам ты %s" % question
    return answers.get(question, default_answer)

def ask_user(answers):
    while True:
        try:
            user_input = input('Поговори со мной! >>  ')
            answer = get_answers(user_input, answers)
            print(answer)

            if user_input == 'пока':
                break
        except KeyboardInterrupt:
            print()
            print('Как жадь, что ты уже уходишь!')
            break    
 
if __name__ == "__main__":        
    ask_user(answers)