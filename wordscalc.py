numbers = {
       "ноль": 0,
       "один": 1,
       "два": 2,
       "три": 3,
       "четыре": 4,
       "пять": 5,
       "шесть": 6,
       "семь": 7,
       "восемь": 8,
       "девять": 9,
       "десять": 10
}

operators = ["плюс", "минус", "умножить", "делить"]


def get_operand(operand_phrase):
    if len(operand_phrase) == 1:
        try:
            return float(numbers[operand_phrase[0]])
        except KeyError:
            return "Нет такого числа {}".format(operand_phrase[0])       
    elif len(operand_phrase)  == 3:
        if operand_phrase[1] == 'и':
            try:
                return float("{}.{}".format(numbers[operand_phrase[0]], numbers[operand_phrase[2]]))
            except KeyError:
                return "Нет такого числа {}.{}".format(operand_phrase[0], operand_phrase[2])
            
        else:
            return "Неизвестный символ \"{}\" в операнде".format(operand_phrase[1])
    else:
        return "Моя твоя не понимать"


def wordscalc(phrase):
       # "три и два плюс один и пять"

    phrase = phrase.split()
    operators_count = 0

    for op in operators:
        if op in phrase:
            operator = op
            index_op = phrase.index(op) 
            if operator in [op for op in operators[2: ]]:
                operand_1_phrase = phrase[0 : index_op]
                operand_2_phrase = phrase[index_op + 2 : ]
            else:
                operand_1_phrase = phrase[0 : index_op]
                operand_2_phrase = phrase[index_op + 1 : ]
            operators_count += 1

    if operators_count == 0:
        return "Не найден оператор"
    elif operators_count > 1:
        return "Найдено больше одного оператора"


    operand_1 = get_operand(operand_1_phrase)
    if isinstance(operand_1, str):
        return operand_1

    operand_2 = get_operand(operand_2_phrase)
    if isinstance(operand_2, str):
        return operand_2


    if operator == "плюс":
        return operand_1 + operand_2
    elif operator == "минус":
        return operand_1 - operand_2
    elif operator == "умножить":
        return operand_1 * operand_2
    elif operator == "делить":
        try:
            return operand_1 / operand_2
        except ZeroDivisionError:
            return "Делить на 0 нельзя!"

if __name__ == "__main__":

       phrase = input("Введите фразу >> ")
       print(wordscalc(phrase))
