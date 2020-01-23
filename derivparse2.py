import sys
import statistics 

input1= sys.argv[1]
fp= open(input1, 'r')

og=[]
for ln in range(120):
    line= fp.readline()
    line= line.replace('\n', '')
    line= float(line)
    og.append(line)

diffarr=[]
for counter in range(20,60):
    val1= og[counter]
    val2= og[counter+1]
    if val1==0:
        val1=1
    if val2==0:
        val2=1
    diff= val2/val1
    diffarr.append(diff)
    split1= max(diffarr)

diffarr2=[]
for counter in range(60,95):
    val1= og[counter]
    val2= og[counter+1]
    if val1==0:
        val1=1
    if val2==0:
        val2=1
    diff2= val2/val1
    diffarr2.append(diff2)
    split2= min(diffarr2)

cutoff1=diffarr.index(split1)+1+20
cutoff2=diffarr2.index(split2)+1+60
print 'cutoff1', cutoff1
print 'cutoff2', cutoff2

stdarr1=[]
sum1=0
length1=0
for idx in range(0, cutoff1):
    sum1+=og[idx]
    length1+=1
    stdarr1.append(og[idx])

stdarr2=[]
sum2=0
length2=0
for idx in range(cutoff1, cutoff2):
    sum2+=og[idx]
    length2+=1
    stdarr2.append(og[idx])
avgdensity2= float(sum2/length2)
stdliq=statistics.stdev(stdarr2)


sum3=0
length3=0
for idx in range(cutoff2, 120):
    sum3+=og[idx]
    length3+=1
    stdarr1.append(og[idx])
stdgas= statistics.stdev(stdarr1)

gaslen= length1 + length3
gassum=sum1+sum3
gasdensity= gassum/gaslen

print gasdensity, avgdensity2
print 'stdgas:', stdgas, 'stdliq:', stdliq


