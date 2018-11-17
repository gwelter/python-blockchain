names = ["Guilherme", "Gustavo", "Ana", "George", "Nicolas", "Nathan", "Jonathan", "Max"]

for name in names:
    if len(name) >= 5:
        if "n" in name or "N" in name:
            print(len(name))

while len(names) > 0:
    print("cleaning: " + str(names))
    names.pop()