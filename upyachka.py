import re

def upyachka_slang(question):
    m = re.match('(пыщ)+[1|!]*$', question)
    if m:
        return "Ололо! Попячся!1"
    else:
        return False

if __name__ == "__main__":
	question = input("Пыщ! >> ")
	print(upyachka_slang(question))