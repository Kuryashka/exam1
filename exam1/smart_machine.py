while True:
    try:
        a = int(input("Enter anu number: "))
        break
    except ValueError:
        continue
if a <= 100:
    print(a - 10)
else:
    print(a - 20)