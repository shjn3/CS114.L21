foot = [[0,-1],[-1,0],[0,1],[1,0]]
head=['<','^','>','v']

def left_right(di,_head):
    if di =='L':
        for i in range(4):
            if _head == head[i]:
                if i == 0:
                    i=3
                    return head[i]
                else:
                    i-=1
                    return head[i]
    elif di =='R':
        for i in range(4):
            if _head == head[i]:
                if i == 3:
                    i=0
                    return head[i]
                else:
                    i+=1
                    return head[i]

def foot_head(ps,di,_head):

    for i in range(4):
        if _head == head[i]:
            x=ps[0]+foot[i][0]
            y=ps[1]+foot[i][1]
            return [head[i],x,y]


def ktra_die(_snake,_head,_array):
    x =_head[1]
    y =_head[2]
    if [x,y] in _snake[:-1]: return 1
    if check_position([x,y],_array) == 0:return 1
    return 0
def check_position(ps,array):
    x = ps[0]
    y = ps[1]
    if x <0 or x >=len(array) or y < 0 or y >=len(array[0]):
        return 0
    return 1
def path_snake(_body,_head):
    snake = []
    _snake=[]
    length = len(_body)
    length+=1
    _head_x=_head[1]
    _head_y=_head[2]
    snake.append([[_head_x,_head_y]])
    
    while snake:
        node = snake.pop()
        if len(node) == length:
            _snake = node
            break
        for i in range(4):
            x = node[-1][0] + foot[i][0] 
            y = node[-1][1] + foot[i][1]
            if [x,y] in _body:
                if [x,y] not in node:
                    snake.append(node+[[x,y]])
    return _snake
def result(_array,_snake,step,_head):
    length = len(_snake)
    for i in step:
        character=_head[0]
        _head_x = _head[1]
        _head_y = _head[2]
        if i =='L' or i == 'R':
            _head[0] = left_right(i,character)
            _array[_head[1]][_head[2]]=_head[0]
        else:
            _head=foot_head([_head_x,_head_y],i,character)

            if ktra_die(_snake,_head,_array):
                for i in _snake:
                    _array[i[0]][i[1]] ='X'
                break
            else:
                if len(_snake)!=1:
                    _array[_snake[-1][0]][_snake[-1][1]]='.'
                    _array[_snake[0][0]][_snake[0][1]]='*'
                    _array[_head[1]][_head[2]]=_head[0]
                    for i in range(length-1,0,-1):
                        _snake[i]=_snake[i-1]
                    _snake[0]=[_head[1],_head[2]]
                else:
                    _array[_snake[-1][0]][_snake[-1][1]]='.'
                    _array[_head[1]][_head[2]]=_head[0]
                    _snake[0]=[_head[1],_head[2]]
def conver(_list):
    string=""
    for i in _list:
        string+=i
    return string



n,m,c=map(int,input().split())
_head=[]
_body=[]
_array=[]
for i in range(n):
    q= input()
    text=[]
    for j in range(m):
        if q[j] in head:
            _head.append(q[j])
            _head.append(i)
            _head.append(j)
        if q[j] == "*":
            _body.append([i,j])
        text.append(q[j])
    _array.append(text)
step=input()
_body=path_snake(_body,_head)
result(_array,_body,step,_head)
for i in _array:
    string = conver(i)
    print(string)
