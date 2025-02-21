import readkeys

print("q: to exit")
while True:
    k = readkeys.getch()
    print((len(k), f"{k}"))
    if k == "q":
        break

