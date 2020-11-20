def addUp(num):
    result = 0
    for i in range(num + 1):
        result = result + i
    print(result)

def addUp2(num):
    result = 0
    half = num  / 2
    result = int((half * num) + half)
    print(result)

addUp(11)
addUp2(11)