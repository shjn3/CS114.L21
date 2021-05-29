def wordUpper(a,color1,color2,color3):
    tmp=a[color1][0]
    a[color1][0]=a[color2][8]
    a[color2][8]=a[color3][4]
    a[color3][4]=tmp
    return a

def wordLower(a,color1,color2,color3):

    b=wordUpper(a,color1,color2,color3)

    tmp1=b[color1][3]
    tmp2=b[color1][2]
    tmp3=b[color1][1]

    b[color1][3]=b[color2][6]
    b[color1][2]=b[color2][7]
    b[color1][1]=b[color2][3]

    b[color2][6]=b[color3][1]
    b[color2][7]=b[color3][5]
    b[color2][3]=b[color3][6]

    b[color3][1]=tmp1
    b[color3][5]=tmp2
    b[color3][6]=tmp3
    return b

def wordUpper_reverse(a,color1,color2,color3):
    tmp=a[color1][0]
    a[color1][0]=a[color2][4]
    a[color2][4]=a[color3][8]
    a[color3][8]=tmp
    return a

def wordLower_reverse(a,color1,color2,color3):

    b=wordUpper_reverse(a,color1,color2,color3)
    

    tmp1=b[color1][3]
    tmp2=b[color1][2]
    tmp3=b[color1][1]

    b[color1][3]=b[color2][1]
    b[color1][2]=b[color2][5]
    b[color1][1]=b[color2][6]

    b[color2][1]=b[color3][6]
    b[color2][5]=b[color3][7]
    b[color2][6]=b[color3][3]

    b[color3][6]=tmp1
    b[color3][7]=tmp2
    b[color3][3]=tmp3
    return b


color = list(map(str,input().split()))
side=[[color[0]]*9,[color[1]]*9,[color[2]]*9,[color[3]]*9]
while True:
    foot = list(map(str,input().split()))
    if foot[0] == '.':
        for i in side:
            for j in i:
               print(j,end=" ")
            print()
        break
    vitri=len(foot)
    for i in range(vitri-1,-1,-1):
        if foot[i].islower():
            if foot[i] == 'u':
               wordLower(side,0,3,2)
            elif foot[i] == "u'":
               wordLower_reverse(side,0,2,3)
            elif foot[i] == 'r':
               wordLower(side,3,0,1)
            elif foot[i] == "r'":
               wordLower_reverse(side,3,1,0)
            elif foot[i] == 'l':
               wordLower(side,2,1,0)
            elif foot[i] == "l'":
               wordLower_reverse(side,2,0,1)
            elif foot[i] == 'b':
               wordLower(side,1,2,3)
            elif foot[i] == "b'":
               wordLower_reverse(side,1,3,2)

        else:
            if foot[i] == 'U':
               wordUpper(side,0,3,2)
            elif foot[i] == "U'":
               wordUpper_reverse(side,0,2,3)
            elif foot[i] == 'R':
               wordUpper(side,3,0,1)
            elif foot[i] == "R'":
               wordUpper_reverse(side,3,1,0)

            elif foot[i] == 'L':
               wordUpper(side,2,1,0)
            elif foot[i] == "L'":
               wordUpper_reverse(side,2,0,1)

            elif foot[i] == 'B':
               wordUpper(side,1,2,3)
            elif foot[i] == "B'":
               wordUpper_reverse(side,1,3,2)
