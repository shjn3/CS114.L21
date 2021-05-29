string = input()
n = int(input())
vt = 0
length=len(string)
_output=""
while vt < length:
    tmp = -1
    tmp = string.find(' ',vt,length)
    _length_tmp=len(_output)
    if tmp!= -1:
        if (_length_tmp+(tmp+1-vt))>n and _output != "":
            if _output[0]!=' ':
                print(_output)
            else:
                print(_output[1:-1])
            _output=string[vt:tmp+1]
        else:
            _output+=string[vt:tmp+1]
        vt=tmp+1
        if vt == length:
            print(_output,end='')
    else:
        if (_length_tmp+(length-vt))>n and _output!="":
           if _output[0]!=' ':
                print(_output)
           else:
                print(_output[1:-1])
           print(string[vt:length],end='')
        else:
            _output+=string[vt:length]+' '
            print(_output,end='')
        break
