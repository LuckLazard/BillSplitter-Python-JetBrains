import random
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
    # print(names)
    
    print("Do you want to use the \"Who is lucky?\" feature? Write Yes/No:\n")
    choice = input()
    if choice == "Yes":
        random_person = random.choice(list(names.keys()))
        print(f"{random_person} is the lucky one!")
    else:
        print("No one is going to be lucky")