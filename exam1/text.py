text = 'The core of extensible programming is defining functions.'
a = text.replace(' ', '')
b = 1
for i in a:
    if b % 2 == 0:
        print(i)
        b += 1
    else:
        b += 1
print(a)
