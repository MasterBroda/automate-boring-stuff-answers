spam = ['apples', 'bananas', 'tofu', 'cats']
s = str()
def listtostr(spam):
    print spam[-1]
    i = spam[-1]
    spam[-1] = "and " + i
    print ', '.join(spam)

listtostr(spam)