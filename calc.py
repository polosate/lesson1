import re

def calc(expr):
	# удаляем пробелы
	expr = expr.replace(' ', '')

	if not expr:
		return "Что считать-то?.."

	# Проверяем, есть ли =. \

	if expr[-1] != "=":
		return "Нет знака ="
	else:
		expr = expr[0:-1]

	# Если в формуле есть не числа и не операторы - ошибка
	for symbol in expr:
		if (not symbol.isdigit()) & (symbol not in '+-*/'):
			return "В формуле есть недопустимые символы."

	# Находим оператор
	operators = list()
	for symbol in expr:
		if not symbol.isdigit():
			operators.append(symbol)
			
	if	len(operators) > 1:
		return "В формуле больше одного оператора"
	elif not operators:
		return "Не найден оператор"
	else:
		operator = operators[0]


	operands = expr.split(operator)
	if len(operands) != 2:
		return "В формуле ошибка"	
	operand_1 = float(operands[0])
	operand_2 = float(operands[1])
	if operator == "+":
		return  operand_1 + operand_2
	elif operator == "-":
		return operand_1 - operand_2
	elif operator == "*":
		return operand_1 * operand_2
	elif operator == "/":
		try:
			return operand_1 / operand_2
		except ZeroDivisionError:
			return "Делить на 0 нельзя!"

				

						


if __name__ == "__main__":
	while True:
		expression = input("Введите формулу >> ")
		print(calc(expression))
