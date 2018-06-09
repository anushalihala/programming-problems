# NOTE: Greedy search fails to give optimal solution in some case
# e.g. if going down snake enables taking another ladder

import heapq as hq
import pdb
from collections import deque

class Priority_Queue:
    def __init__(self):
        self.order = []         #stores order of elements in Priority_Queue (hash values of elements stored in max heap). Heap ordered by i)cost of element ii) element's count)
        self.storage=dict()     #dict stores elements in Priority_Queue to improve performance of element search
        self.counter=0          #number of elements in Priority_Queue
    
    def isEmpty(self): 
        return len(self.storage) == 0    

    def enqueue(self,s):
        tile_val=s.getstate()
        if tile_val not in self.storage:
            hq.heappush(self.order, (-1*tile_val, self.counter) );    #counter is used for ordering (since it is unique) if tile value is same
            self.storage[tile_val]=s                                  #store state in dictionary
        self.counter=self.counter+1    

    def dequeue(self):
        tv,c=hq.heappop(self.order)
        tv=tv*-1
        return self.storage.pop(tv,None)    

class Queue:
    def __init__(self):
        self.order = deque([])  #stores order of elements in Queue (elements stored in FIFO deque)
        self.storage=dict()     #stores elements in Queue to improve performance of element search
    
    def isEmpty(self): 
        return len(self.order) == 0    

    def enqueue(self,s):
        tile_val=s.getstate()
        if tile_val not in self.storage:
            self.order.appendleft(tile_val)  #add to tail of FIFO deque
            self.storage[tile_val]=s         #store element in dictionary

    def dequeue(self):
        #return self.storage[self.order.pop()]
        return self.storage.pop(self.order.pop(),None)
        
class State:

    def __init__(self, initstate, in_level,in_parent): # , in_change):
        #value of tile
        self.mystate=initstate
        
        #state's level in search tree
        self.level=in_level
        
        #reference to state's parent
        self.parent=in_parent
        
        #blank tile's change of position from parent to child (value of dice) -> 1,2,3,4,5 or 6
        # self.change=in_change

    def __str__(self):
        return str(self.__dict__)

    def __eq__(self, other): 
        return self.mystate==other.mystate
        
    def __hash__(self): 
        return hash(self.mystate)
    
    def createchildren(self,ladders_n_snakes,last_tile):
        children=[]
        
        for i in range(1,7):
            endval=self.mystate+i
            
            if(endval>last_tile):
                continue
            
            if(endval in ladders_n_snakes):
                endval=ladders_n_snakes[endval]

            children.append(State(endval,self.level+1,self))
            
        return children
        
    def getstate(self):    
        return self.mystate
    
    def getlevel(self):
        return self.level
        
    def pathtoroot(self):
        path=[]
        curr_state=self
        while curr_state is not None:
            path.append(curr_state.getstate())
            curr_state=curr_state.parent
        path.reverse()    
        return path

def greedySearch(init_state, goal_state, ladders_and_snakes):
    
    frontier = Priority_Queue()
    frontier.enqueue(init_state)
    
    explored = set() #set is unordered collection of unique elements, enables faster searches
    
    while not frontier.isEmpty():   
        curr_state=frontier.dequeue()
        explored.add(curr_state)
        
        if curr_state.getstate()==goal_state:
		
            print(curr_state.pathtoroot())
            return curr_state.getlevel()
            
        for child in curr_state.createchildren(ladders_and_snakes,goal_state):
                
            if child not in explored:
                #enqueue checks if child already in queue, if not child is added
                frontier.enqueue(child) 
                
    return -1
    
def BFS(init_state, goal_state, ladders_and_snakes):
    
    frontier = Queue() 
    frontier.enqueue(init_state)
    
    explored = set() #set is unordered collection of unique elements, enables faster searches
    
    while not frontier.isEmpty():   
        curr_state=frontier.dequeue()
        explored.add(curr_state)
        
        if curr_state.getstate()==goal_state:
		
            print(curr_state.pathtoroot())
            return curr_state.getlevel()
            
        for child in curr_state.createchildren(ladders_and_snakes,goal_state):
                
            if child not in explored:
                #enqueue checks if child already in queue, if not child is added
                frontier.enqueue(child) 
                
    return -1
                
def quickestWayUp(ladders, snakes):
    #converting to dictionaries
    # snakes=[[99,2],[98,2],[96,2],[95,2],[94,2]]
    # ladders=[]
    special_cells=dict()
    for item in ladders:
        special_cells[item[0]]=item[1]
        
    for item in snakes:
        special_cells[item[0]]=item[1]
    
    return BFS(State(1,0,None), 100, special_cells)

#TESTCASES
# ladders=[[32, 62], [42, 68], [12, 98]]
# snakes=[[95, 13], [97, 25], [93, 37], [79, 27], [75, 19], [49, 47], [67, 17]]
ladders= [[8, 52], [6, 80], [26, 42], [2, 72]]
snakes= [[51, 19], [39, 11], [37, 29], [81, 3], [59, 5], [79, 23], [53, 7], [43, 33], [77, 21]]
print(quickestWayUp(ladders,snakes))
