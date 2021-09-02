import math
"create bat imitaion call"
from numpy import pi, sin


def getExpArg(fStart,fEnd,BatCallConstant):
    return (BatCallConstant*fEnd)/fStart
" getCallVal returns value of bat imitaion call"
def getCallVal(i,fStart,fEnd,BatCallConstant):
    fr=192000
    t = float(i)/fr*100
    fStart=fStart/100
    fEnd=fEnd/100
    amp=32767. /2.
    arg=getExpArg(fStart,fEnd,Bat)
    return amp*sin(2.*pi*((fStart/(fStart-BatCallConstant*fEnd))*((fStart-fEnd)*math.pow(arg, t)/math.log(arg)+(1-BatCallConstant)*fEnd*t)))

def 