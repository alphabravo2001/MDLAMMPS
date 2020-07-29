step=[]
elap=[]
temp=[]
press=[]
vol=[]
tote=[]
kine=[]
pote=[]
emol=[]
epair=[]
pxx=[]
pyy=[]
pzz=[]
pxy=[]
pxz=[]
pyz=[]

data=[]

from statistics import mean,stdev
import sys
import numpy

input= sys.argv[1]
counter=0

fp= open(input, 'r')
while fp.readline().split()[0]!='Step':
    continue

title=fp.readline().split()

while fp.readline()!='':
    line= fp.readline().split()
    #print (line)
    #print (len(line))
    if line:
        for idx in range(len(line)):
            line[idx]=float(line[idx])
        step,elap,temp,press,vol,tote,kine,pote,emol,epair,pxx,pyy,pzz,pxy,pxz,pyz=line
        data.append(line)

arr=numpy.empty([len(data),2])
#output=sys.argv[2]
for idx in range(len(data)):
    arr[idx, 0]=mean(data[idx])
    arr[idx, 1]=stdev(data[idx])

print (arr)
    
#numpy.savetxt(output,arr)