str=input('Enter the word')
s=str.split(' ')
str1=''
for j in s:
    l=len(j)
    if j[0] in ('a','e','i','o','u'):
        j=j+'ay'
        print(j,end=' ')
    else:
        if (j[1]=='q') and (j[2]=='u'):
            n = 3
            while (n < l):
                str1 = str1 + j[n]
                n = n + 1
            str1 = str1 + j[0]+j[1]+j[2]
            str1 = str1 + 'ay'
            print(str1,end='')

        else:
            i=0
            k=0
            for p in j:

                if p not in ('a','e','i','o','u'):
                    i=i+1
                    m=i
                    continue
                else:

                    while(i<l):
                        str1=str1+j[i]
                        i=i+1
                    while(k<m):
                        str1=str1+j[k]
                        k=k+1

                str1=str1+'ay'
                print(str1,end='')
                break













