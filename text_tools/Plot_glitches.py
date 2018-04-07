import io

f = io.open("plot.txt", mode="r", encoding="utf8")
text = f.read()
print(u'{}'.format(text))
# with open('plot.txt', , encoding="utf-8") as f:
#     words = f.read().splitlines()
#     print(u''.join(words))