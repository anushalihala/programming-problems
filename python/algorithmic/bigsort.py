import pdb
    
unsorted=['1','30','2','20','10']           #INPUT ARRAY

str_lengths=[len(i) for i in unsorted]      #number of digits
str_lengths = list(enumerate(str_lengths))
sort_by_len=[]
for i,j in str_lengths:                     #reverse tuples
    sort_by_len.append((j,i))
    
sort_by_len.sort()

prev=sort_by_len[0][0]
sortedlist=[]
lst=[]
for l,idx in sort_by_len:
    
    if(l==prev):
        lst.append(unsorted[idx])
    else:
        
        lst.sort()
        
        sortedlist.extend(lst)
        lst=[unsorted[idx]]
        prev=l

lst.sort()
sortedlist.extend(lst)        
print(sortedlist)

