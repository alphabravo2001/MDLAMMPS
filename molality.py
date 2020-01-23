import sys
import numpy
#coding= utf-8

input1= sys.argv[1]  #density table
input2= sys.argv[2] #lammpstraj.]
output= sys.argv[3]
output2= sys.argv[4]
output3= sys.argv[5]

arr=[]
arr1=[]
arr2=[]
arr3=[]
arr4=[]
avgc = 6.022140857 * (10 ** 23)

fp = open(input1, 'r')
fc = open(input2, 'r')

scanlines= len(fc.readlines())
print 'number of lines:', scanlines
fc.seek(0,0)

counter=0
for ln in range(scanlines):
    lnscan=fc.readline()
    lnscan=lnscan.replace('\n','')
    if lnscan== 'ITEM: TIMESTEP':
        counter+=1

print 'number of configurations:', counter
fc.close()

for ln in range(120):
    line= fp.readline() 
    arr.append(line)
    arr[ln]= arr[ln].replace('\n','')
    arr[ln]= arr[ln]. split(' ')
    for idx in range(len(arr[ln])):
        arr[ln][idx]= float(arr[ln][idx])
    arr1.append(arr[ln][2])
    arr2.append(arr[ln][3])
    arr3.append(arr[ln][4])
    arr4.append(arr[ln][5])
    
totO = sum(arr1)  #number of water molecules=number of oxygen
mwater=totO*18.015 #total mass of solvent 

nsol = sum(arr3)/avgc
msol = (sum(arr1))/avgc * 0.01801
molality = nsol/msol  
print molality

fp.close() 

#volume cal

fc = open(input2, 'r')
line2 = fc.readline()
line2 = fc.readline()
line2 = fc.readline()
line2 = fc.readline()
line2 = fc.readline()
#x range
line2 = fc.readline()
x =line2.replace('\n','')
x =x.split(' ')
x[1] = float(x[1])
x[0] = float(x[0])
xmult = x[1]-x[0]
print 'xmult: ', xmult
#y range
line2 = fc.readline()
y = line2.replace('\n','')
y = y.split(' ')
y[1] = float(y[1])
y[0] = float(y[0])
ymult = y[1]-y[0]
print 'ymult: ', ymult
#z range
line2 = fc.readline()
z = line2.replace('\n','')
z = z.split(' ')
z[1] = float(z[1])
z[0] = float(z[0])
zmult = z[1]-z[0]
dz = zmult/120
print 'zmult: ', zmult

#calcualting volumber per bin
binvolang=xmult*ymult*dz

bindensity=[]
for idx in range(120):
    binmass = (arr1[idx]* 16.)+ (arr2[idx]*1.007)+ (arr3[idx]* 22.98)+ (arr4[idx]* 35.45)
    bindensitygcc = binmass/binvolang*(10 ** 24)/avgc/counter
    bindensity.append(bindensitygcc)

print bindensity
fc.close()


deriv1=[]
for counter in range(119):
    val1 = bindensity[counter]
    val2 = bindensity[counter+1]
    diff = val2-val1
    deriv1.append(diff)
npderiv1= numpy.asarray(deriv1)
numpy.savetxt(output2, npderiv1)
deriv2=[]
for counter2 in range(118):
    val3 = deriv1[counter2]
    val4 = deriv1[counter2+1]
    diff2 = val4-val3
    deriv2.append(diff2)
npderiv2= numpy.asarray(deriv2)
numpy.savetxt(output3,npderiv2)

print deriv1
print deriv2
split1 = max(deriv2)
split2 = min(deriv2)
print 'split 1 bin', deriv2.index(split1)
print 'split 2 bin', deriv2.index(split2)

npbindensity= numpy.asarray(bindensity)
numpy.savetxt(output,npbindensity)
