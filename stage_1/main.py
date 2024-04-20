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
    print(names)