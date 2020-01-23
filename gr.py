import sys 
import numpy

trajarr=[]
probarr=[]
trajarr2=[]

def initializeconfig():
    global fp
    line = fp.readline()
    line = fp.readline() # TS
    line = fp.readline() # atoms
    line = fp.readline() # num atoms
    natoms= int(line)
    line = fp.readline()
    line = fp.readline()
    x=line.replace('\n', '')
    x=x.split(' ')
    x[1]=float(x[1])
    x[0]=float(x[0])
    xmult= x[1]-x[0]
    line = fp.readline()
    y=line.replace('\n', '')
    y=y.split(' ')
    y[1]=float(y[1])
    y[0]=float(y[0])
    ymult= y[1]-y[0]
    line = fp.readline() #z range
    z=line.replace('\n','')
    z=z.split(' ')
    z[1]=float(z[1])
    z[0]=float(z[0])
    zmult= z[1]-z[0]
    line = fp.readline()
    return [natoms,xmult,ymult,zmult]
    
def grccalc(natoms,xmult,ymult,zmult):
    global trajarr 
    global trajarr2
    global fp
    with open(input, 'r') as fc:
        for ln in range(natoms):
            arr=[0,0,0,0]
            line= fp.readline()
            line= line.replace('\n', '')
            line= line.split(' ')
            for idx in range(len(line)):
		line[idx]=float(line[idx])
            arr[0]= line[1]
            arr[1]= line[2]*xmult
            arr[2]= line[3]*ymult
            arr[3]= line[4]*zmult
            trajarr.append(arr)
    
	for idx in range(len(trajarr)):
             if trajarr[idx][0]== 1.0:
                  trajarr2.append(trajarr[idx])
       	          
    trajlen= len(trajarr2)
    vectorarr= numpy.zeros((len(trajarr2),3))
    for atom in range(trajlen):
         vectorarr[atom][0]= trajarr2[atom][1]
         vectorarr[atom][1]= trajarr2[atom][2]
         vectorarr[atom][2]= trajarr2[atom][3]
    print vectorarr
    j=0
    while j < (len(vectorarr)-1):
        for i in range(j+1,len(vectorarr)):
            x=numpy.linalg.norm(vectorarr[i]-vectorarr[j])
            probarr.append(x)
        j+=1
  
    trajarr=[]
    trajarr2=[]

#--------------------------------------------------------------
input= sys.argv[1]     #traj file
outfile=sys.argv[2]
fp= open(input, 'r')

scanlines= len(fp.readlines())
print 'number of lines:', scanlines
fp.seek(0,0)

counter=0
for ln in range(scanlines):
    lnscan=fp.readline()
    lnscan=lnscan.replace('\n','')
    if lnscan== 'ITEM: TIMESTEP':
        counter+=1
print 'number of configurations:', counter 
fp.seek(0,0)
    
for x in range(counter):
    dataarr= initializeconfig()
    grccalc(dataarr[0], dataarr[1], dataarr[2], dataarr[3])
    print 'traj done' ,x

probarr2=numpy.asarray(probarr)

numpy.savetxt(outfile,probarr)
