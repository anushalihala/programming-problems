import math
import sys
import os

def sectionOnes(msb_pow):
    global number_of_ones
    ans=number_of_ones.get(msb_pow,-1)
    
    if(ans<0): 
        ans=2**msb_pow
        ans=ans+(msb_pow*ans/2)
        number_of_ones[msb_pow]=ans
        
    return ans
    
def partialSectionOnes(num):
    if(num<1):
        return (0,0)
    
    msb_pow=math.floor(math.log(num,2)) 
    sum=0
    prob=0
    
    for i in range(msb_pow):
        ans=sectionOnes(i)
        sum=sum+ans
        prob=prob+(ans/(i+1))
    
    msb=2**msb_pow
    diff=num - msb
    
    this_section=diff+1
    (result,p)=partialSectionOnes(diff)
    this_section=this_section+result
    sum=sum+this_section
    prob=prob+(this_section/(msb_pow+1))
    return (sum,prob)
    
def integerOnes(a,b):
    a_results=partialSectionOnes(a-1)
    b_results=partialSectionOnes(b)
    
    probability=b_results[1] - a_results[1]
    expectation=b_results[0] - a_results[0]

    interval=b-a+1
    p=1/interval
    
    probability=probability*p
    expectation=expectation*p
    
    return(probability,expectation)
    
if __name__ == '__main__':
    global number_of_ones
    number_of_ones=dict()
    
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # t = int(input())

    # for t_itr in range(t):
        # ab = input().split()

        # a = int(ab[0])

        # b = int(ab[1])

        # result = integerOnes(a, b)
        
        # if(t_itr!=0):
            # fptr.write('\n')
            
        # ffptr.write('{:.5f} {:.5f}'.format(result[0],result[1]))

    # fptr.close()
     
    a=16493744
    b=39146561
    print(integerOnes(a,b))