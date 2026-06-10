import random
import customtkinter
''''dmgPlotter functions'''
def MUn(n,s):
    return(.5*n*(s+1))
def sigSquared(n,s):
    MU1 = MUn(1,s)
    return(n*(((1/6)*(s+1)*((2*s)+1))-(MU1**2)))
def numberDistribution(x,sigma,MU):
    returnNumber = (1/(2*3.1415926*sigma))*(2.71828**(-.5*(((x-MU)/sigma)**2)))
    return(returnNumber)
def hitModifier(theDC,theSave):
    return((theDC-theSave-1)/20)

