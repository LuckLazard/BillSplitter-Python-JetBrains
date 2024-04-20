print("Enter the number of friends joining (including you):\n")
num = int(input())
if num <= 0:
    print("No one is joining for the party")
else:
    names = {}
    while num != 0:
        x = input()
        names[x] = 0
        num -= 1

    print("Enter the total bill value:\n")
    x = int(input())
    for person in names.keys():
        names[person] = round(x / len(names), 2)
    print(names)