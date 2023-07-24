def average_for():
    ages = []  # list in which we store all the values
    while True:
        x = input("Enter age: ")  # takes input one by one
        if x == '':  # checks that the input is not ENTER (no more numbers)
            break
        ages.append(x)  # if input is actually a number it adds it to the list

    sum = 0
    for i in ages:  # takes every age, adds it to the sum
        sum += int(i)
    else:
        print(sum/len(ages))  # if for is finished, prints out the average

# average_for()


def average_while():
    ages = []  # list in which we store all the values
    while True:
        x = input("Enter age: ")  # takes input one by one
        if x == '':  # checks that the input is not ENTER (no more numbers)
            break
        ages.append(x)  # if input is actually a number it adds it to the list

    sum = 0
    n = len(ages) - 1

    while n:
        sum += int(ages[n])
        n -= 1
    else:
        print(sum/len(ages))

# average_while()


def sort_for():
    names = []  # list that stores all names
    while True:
        s = input("Enter name: ")  # takes each name as input
        if s == '':  # if it's not ENTER
            break
        names.append(s)  # adds it to the list

    l = len(names)

    for i in range(l - 1):  # bubble sort
        for j in range(i + 1, l):
            # if names[i] is after names[j], it switches the two using temp (checks with lowercase so it doesn't take
            # into consideration capitalization)
            if names[i].lower() > names[j].lower():
                temp = names[i]
                names[i] = names[j]
                names[j] = temp
    else:
        print(names)  # when for is finished, it prints the now srorted list

# sort_for()

def sort_while():
    names = []
    while True:
        s = input("Enter name: ")
        if s == '':
            break
        names.append(s)

    i = 0
    l = len(names)
    while (i < l - 1):  # bubble sort but with two whiles instead of two for s
        j = i
        while (j < l):
            if names[i].lower() > names[j].lower():
                temp = names[i]
                names[i] = names[j]
                names[j] = temp
            j += 1
        i += 1
    else:
        print(names)

sort_while()