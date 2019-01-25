from numpy import *

s = '9193	0.510310	0.016395	smallDoses'
ss = s.split('\t')
returnMat = zeros((2,3))
returnMat[0,:] = ss[0:3]
print(returnMat)
