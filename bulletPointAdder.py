import pyperclip
text = pyperclip.paste()

print text

l = list()
l = text.split("\n")
print "~~~~~~~~~~"
text = "".join(["* " +i for i in l])
print text
pyperclip.copy(text)