a = 10 
def FloatToString (aFloat):
    if type(aFloat) != float:
        return ""
    strTemp = str(aFloat)
    strList = strTemp.split(".")
    if len(strList) == 1 :
        return strTemp
    else:
        if strList[1] == "0" :
            return strList[0]
        else:
            return strTemp

def b():
    pass
 
print isinstance(a,(int,str))
print isinstance(a,(float,str))
print isinstance(b,(str,int))

print FloatToString(a)