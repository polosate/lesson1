def countwords(phrase):
     for char in phrase:
        if char in "?.,!/;:()*%\"\'":
            phrase = phrase.replace(char, ' ')

     return len(phrase.split()) - 1


if __name__ == "__main__":
     phrase = input("Напиши фразу >> ")
     print(countwords(phrase))
