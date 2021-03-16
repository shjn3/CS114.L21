def ktratinhtu(str):
    leng = len(str)
    if leng < 4:
        return -1
    elif leng == 4:
        if x == "lios":
            return 1
    elif leng ==5:
        if x[leng-4:leng] == "lios":
            return 1
        elif x == "liala":
            return 2
    else:
        if x[leng-4:leng] == "lios":
            return 1
        elif x[leng-5:leng] == "liala":
            return 2
    return -1
    
def ktradanhtu(str):
    leng = len(str)
    if leng < 3:
        return -1
    elif leng == 3:
        if x == "etr":
            return 1
    elif leng == 4:
        if x[leng-3:leng]=="etr":
            return 1
        if x == "etra":
            return 2
    else:
        if x[leng-3:leng] == "etr":
            return 1
        elif x[leng-4:leng] == "etra":
            return 2
    return -1

def ktradongtu(str):
    leng = len(str)
    if leng < 6:
        return -1
    elif leng == 6:
        if x == "initis":
            return 1
        elif x == "inites":
            return 2
    else:
        if x[leng-6:leng] == "initis":
            return 1
        elif x[leng-6:leng] == "inites":
            return 2
    return -1

str = input()
tmp = str.split()
ktra = len(tmp)
truocdo = -1
nam = 0
nu = 0
danhtu = 0
tinhtu = 0
dongtu = 0
for x in tmp:
    if ktratinhtu(x) == 1:
        tinhtu+=1
        nam+=1
        if truocdo == 2 or truocdo ==3:
            print("NO")
            exit()
        truocdo = 1
    elif ktratinhtu(x) == 2:
        tinhtu+=1
        nu+=1
        if truocdo == 2 or truocdo ==3:
            print("NO")
            exit()
        truocdo = 1
    elif ktradanhtu(x) == 1:
        danhtu+=1
        nam+=1
        if truocdo == 3 or truocdo == 2 or danhtu == 2:
            print("NO")
            exit()
        truocdo = 2
    elif ktradanhtu(x) == 2:
        if truocdo == 3 or truocdo == 2:
            print("NO")
            exit()
        truocdo = 2
        danhtu+=1
        nu+=1
    elif ktradongtu(x) == 1:
        if danhtu == 0:
            print("NO")
            exit()
        truocdo = 3
        dongtu+=1
        nam+=1
    elif ktradongtu(x) == 2:
        if danhtu == 0:
            print("NO")
            exit()
        truocdo = 3
        dongtu+=1
        nu+=1
            
if nam != ktra and nu != ktra:
    print("NO")
else:
    print("YES")
