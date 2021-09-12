import pdb

#finds all combinations in arr
def combinations(arr):
    l=len(arr)
    lst=[]
    if (l==1):
        return [arr]
    else:
        subcomb = combinations(arr[1::])
        
        for item in subcomb:
            sublst=[arr[0]]
            sublst.extend(item)  
            lst.append(sublst)
            
        lst.append([arr[0]])
        lst.extend(subcomb)
            
        return lst
        
#finds all combination sums in arr        
def comb_sum(arr):
    l=len(arr)
    lst=[]
    if (l==1):
        return arr
    else:
        subsum = comb_sum(arr[1::])
        
        for item in subsum:
            sub=arr[0]+ item
            lst.append(sub)
            
        lst.append(arr[0])
        lst.extend(subsum)
            
        return lst       
        
#print all combination in arr (v2)       
def print_combinations(arr, acc):
    l=len(arr)
    if(l==1):
        print(acc+[arr[0]])
    else:
        new_acc=acc+[arr[0]]
        print(new_acc)
        
        print_combinations(arr[1::],acc)
        print_combinations(arr[1::],new_acc)
       
#print all combination sums in arr (v2)      
def print_sum(arr, acc):
    l=len(arr)
    if(l==1):
        print(acc+arr[0])
    else:
        new_acc=acc+arr[0]
        print(new_acc)
        
        print_sum(arr[1::],acc)
        print_sum(arr[1::],new_acc)


#SOLUTIONS        
#bruteforce: maximum %m for all combination sums in arr 
def found_max(num,m):
    #have found maximum possible %m value
    if(num==m-1):
        return True
    else:
        return False

def max_sum_mod(arr, acc_mod, max_mod, m):
    l=len(arr)
    if(l==1):
        new_mod=(acc_mod+arr[0])%m
        print(new_mod)
        if(new_mod>max_mod):
            return new_mod
        else:
            return max_mod
    else:
        new_mod=(acc_mod+arr[0])%m
        print(new_mod)
        
        new_max_mod=max_mod
        if(new_mod>new_max_mod):
            new_max_mod=new_mod
        
        if(found_max(new_max_mod,m)):
            return new_max_mod
        
        new_max_mod = max_sum_mod(arr[1::],acc_mod,new_max_mod,m) 
        
        if(found_max(new_max_mod,m)):
            return new_max_mod
        
        new_max_mod = max_sum_mod(arr[1::],new_mod,new_max_mod,m) 
        
        if(found_max(new_max_mod,m)):
            return new_max_mod
            
        return new_max_mod
        
def maximumSum1(a, m):
    total=sum(a)
    if(total<m):
        return total
    else:
        return max_sum_mod(a,0,0,m)
     
     
#Dynamic programming
def f(arr, n, c, m):
    #n=len(arr) (ALTERNATIVE)
    key=str(n)+','+str(c)
    global dynamic_values
    
    if(n==0 or c==0):
        dynamic_values[key]=0
        return 0
    
    total=sum(arr)
    if(total<c):
        return total
    
    key1=str(n-1)+','+str(c)
    val1=dynamic_values.get(key1,-1)
    
    if(val1<0):
        val1=f(arr[1::],n-1,c,m)
        
    if(found_max(val1,m)):
        return val1
        
    new_c = c-(arr[0]%m)
    val2=0
    
    if(not new_c<0):
        key2=str(n-1)+','+str(new_c)
        val2=dynamic_values.get(key2,-1)
        if(val2<0):
            val2=f(arr[1::],n-1,new_c,m)
        val2=(val2+arr[0])%m
    
    if(val1>val2):
        dynamic_values[key]=val1
        return val1
    else:
        dynamic_values[key]=val2
        return val2
            
def maximumSum2(a, m):
    global dynamic_values 
    dynamic_values = dict()
    return f(a,len(a),m-1,m)
  
# [4,3,1,2,5,100,5]       
aa=[4,4,4,3,1,2,5,100,5]  
mm=120
print('ans1',maximumSum1(aa,mm))
print('ans2',maximumSum2(aa,mm))
