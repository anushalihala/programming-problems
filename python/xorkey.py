import pdb
import heapq as hq

#SOLUTION: Using heaps
def xorKeyHeap(x,queries):
    ans=[]
    for q in queries:
        heap=[]
        for i in range(q[1]-1,q[2]):
            result=q[0]^x[i]
            hq.heappush(heap,-1*result)
        ans_q=hq.heappop(heap)*-1
        ans.append(ans_q)
    return ans

#SOLUTION: For finding maximum XOR value in whole array (for previous version of Trie)
def xorKey2(x,queries):
    ans=[]
    for q in queries:
        t=Trie()
        for i in range(q[1]-1,q[2]):
            t.insert(x[i],i+1)
        ans.append(t.maxMod(q[0]))
    return ans

#SOLUTION: Using Tries    
class TrieNode:
    def __init__(self):
        self.pointer0=None
        self.pointer1=None
        self.index_0=[]
        self.index_1=[]

    def __str__(self):
        return str(self.__dict__)
        
    def __repr__(self):
        return str(sum(list(map(int,list(str(id(self)))))))
    
class Trie:
    def __init__(self):
        self.root_node = TrieNode()
        self.trie_height=0
        
    def __str__(self):
        return str(self.__dict__)
        
    def insert(self, num, idx):
        binary_string=bin(num)[2::]
        bin_length=len(binary_string)
        
        if(self.trie_height==0):
            #update trie height and directly insert num
            self.trie_height=bin_length
        
        if(bin_length<self.trie_height):
            diff=self.trie_height-bin_length
            padding='0'*diff
            binary_string=padding+binary_string
            
        elif(bin_length>self.trie_height):
            diff=bin_length-self.trie_height
            padding='0'*diff
            new_root=TrieNode()
            all_indexes= self.root_node.index_0 + self.root_node.index_1
            end_node = self.insertEqual(new_root,padding,all_indexes)
            
            end_node.pointer0=self.root_node.pointer0
            end_node.pointer1=self.root_node.pointer1
            end_node.index_0=self.root_node.index_0
            end_node.index_1=self.root_node.index_1
            
            self.root_node=new_root
            self.trie_height=bin_length
            
        pointer=self.root_node    
        self.insertEqual(pointer,binary_string,[idx])
        
    def insertEqual(self,starting_node, binary_num, idx):
        #trie is empty or
        #length of binary_num = height of trie
        pointer=starting_node
        
        for i in range(len(binary_num)):
            if(binary_num[i]=='0'):
                pointer.index_0.extend(idx) 
                
                if(pointer.pointer0 is None):
                    pointer.pointer0=TrieNode()
                
                pointer=pointer.pointer0
            
            else:
                pointer.index_1.extend(idx) 
                
                if(pointer.pointer1 is None):
                    pointer.pointer1=TrieNode()
                
                pointer=pointer.pointer1

        return pointer
        
    def printTrie(self, current_node=None):
        if(current_node is None):
            current_node=self.root_node
        print(repr(current_node), current_node)
        if(current_node.pointer0 is not None):
            self.printTrie(current_node.pointer0)
        if(current_node.pointer1 is not None):
            self.printTrie(current_node.pointer1)
   
    def maxMod(self,num,lb,ub):
    
        binary_string=bin(num)[2::]
        bin_length=len(binary_string)
        ans=''

        if(bin_length<self.trie_height):
            diff=self.trie_height-bin_length
            padding='0'*diff
            binary_string=padding+binary_string           
        elif(bin_length>self.trie_height):
            diff=bin_length-self.trie_height
            ans=binary_string[0:diff] # x xor 0 = x
            binary_string=binary_string[diff::]
            
        bin_length=len(binary_string)
        pointer=self.root_node
        
        for i in range(bin_length):
            if(binary_string[i]=='1'):
            
                if((pointer.pointer0 is not None) and (self.withinRange(pointer.index_0,lb,ub))):
                    pointer=pointer.pointer0
                    ans=ans+'1'
                else:
                    pointer=pointer.pointer1
                    ans=ans+'0'
            
            else:
                
                if((pointer.pointer1 is not None) and (self.withinRange(pointer.index_1,lb,ub))):
                    pointer=pointer.pointer1
                    ans=ans+'1'
                else:
                    pointer=pointer.pointer0
                    ans=ans+'0'
            
        return int(ans,2)
        
    def withinRange(self,num_arr,l,r):
        for element in num_arr:
            if(l<=element and element<=r):     
                return True
        return False
       
def xorKey(x,queries):
    ans=[]
    t=Trie()
    for i,element in enumerate(x):
        t.insert(element,i+1)
            
    for q in queries:     
        ans.append(t.maxMod(q[0],q[1],q[2]))
    return ans

#TEST CASES
arr=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
q_list=[[10, 6, 10], [1023, 7, 7], [33, 5, 8], [182, 5, 10], [181, 1, 13], [5, 10, 15], [99, 8, 9], [33, 10, 14]]
print(xorKeyHeap(arr,q_list))
print(xorKey(arr,q_list))

#TESTING
# t=Trie()
# t.insert(6,2)
# t.printTrie()
# print('\n')
# t.insert(8,3)
# t.printTrie()
# print('\n')
# t.insert(9,4)
# t.printTrie()
# print('\n')
# t.insert(1,5)
# t.printTrie()

# print(t.maxMod(2))
# print(t.maxMod(6))
# print(t.maxMod(16))
