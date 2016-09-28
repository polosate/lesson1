from googlesearch import googlesearch

answers = {
    'привет': 'И тебе привет!',
    'как дела': 'Лучше всех!',
    'пока': 'Увидимся!'
}

def get_answers(question, answers):
    question = question.lower().strip()
    question_without_punctuation = question
    
    for char in question_without_punctuation:
        if char in "?.!/;:()*%\"\'":
            question_without_punctuation = question_without_punctuation.replace(char, '')

    if question_without_punctuation == '':
        return "Да тут одни знаки пунктуации! Пиши словами!"
    
    if question_without_punctuation not in answers:
        if question[-1] == "?":
            return("А почему ви спгашиваете?")
        else:
            return googlesearch(question)
    else:
        return answers.get(question_without_punctuation)


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
