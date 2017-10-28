import sys

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
 
def test_for():
    for x in xrange(0,10):
        print(x);

def test_path():
    print sys.path[0]
    #hh = 122;
    tt=322
    tem='%f' %tt
    print tem

print isinstance(a,(int,str))
print isinstance(a,(float,str))
print isinstance(b,(str,int))

print FloatToString(a)
#test_for();
test_path()