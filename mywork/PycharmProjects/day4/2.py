dat=input('Enter the date in dd-mm-yy form')
l=[]
l=dat.split('-')
mnth={1:'Jan',2:'Feb',3:'Mar',4:'April',5:'May',6:'Jun',7:'Jul',8:'Aug',9:'Sept',10:'Oct','11':'Nov','12':'Dec'}
k=int(l[1])
print(l[0],mnth[k],1900+int(l[2]))
