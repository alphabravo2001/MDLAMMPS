import sys
import numpy
import matplotlib.pyplot

i=0 #array counter
arrtable=[]
bincount=120 
zcoldict={}
    
def initializeconfig():
    global fp
    line = fp.readline()
    line = fp.readline() # TS
    line = fp.readline() # atoms
    line = fp.readline() # num atoms
    natoms= int(line)
    line = fp.readline()
    line = fp.readline()
    line = fp.readline()
    line = fp.readline() #z range
    z=line.replace('\n','')
    z=z.split(' ')
    z[1]=float(z[1])
    z[0]=float(z[0])
    zmult= z[1]-z[0]
    line = fp.readline()
    return [zmult, natoms]

def readconf(numlines, zmultiplier):
    global arrtable
    global i
    global fp
    global zlist 
    global zcoldict
    
    binlength= zmultiplier/120

    for x in range(numlines):
        arrtable.append(fp.readline())
        arrtable[i]= arrtable[i].replace('\n','')
        arrtable[i]= arrtable[i].split(' ')
        
        for idx in range(len(arrtable[i])):
            arrtable[i][idx]= float(arrtable[i][idx])
        #converting into bin array
            if 0<=arrtable[i][4]<=1:
                arrtable[i][4]*= zmultiplier
        i+=1
   
    for znum in range(len(arrtable)):
        zval= arrtable[znum][4]
        atomval= arrtable[znum][1]
        zcoldict[zval] = atomval
  
        binval= int(zval / binlength)
        zlist[binval-1][1]+=1
        zlist[binval-1][int(atomval)+1]+= 1
        zcoldict={} # resetting zcoldict for next line 
    
    for idx in range(bincount):
        zlist[idx][0]=idx*(zmulti/120)
    
    #resetting for next config
    i=0
    arrtable=[]
    binvalarr=[]
    

if __name__ == "__main__":
    counter=0
    
    fileinput= sys.argv[1]
    fileoutput=str(sys.argv[2])
    fp= open(fileinput, "r")
    
    scanlines= len(fp.readlines())
    print 'number of lines:', scanlines
    fp.seek(0,0)
            
    for ln in range(scanlines):
        lnscan=fp.readline()
        lnscan=lnscan.replace('\n','')
        if lnscan== 'ITEM: TIMESTEP':
            counter+=1
    
    print 'number of configurations:', counter
    fp.seek(0,0)
    
    returnarr=[0,0]
   
    zlist= [[0 for countnum in range(6)] for binnum in range(bincount)]  
    
    for x in range(counter):
        returnarr= initializeconfig()
        zmulti= returnarr[0]
        natoms= returnarr[1]
        readconf(natoms,zmulti)
    
    print zlist
    sum1=0
    for idx in range(len(zlist)):
        sum1+= zlist[idx][1]

    print sum1

    numpy.savetxt(fileoutput, zlist)
