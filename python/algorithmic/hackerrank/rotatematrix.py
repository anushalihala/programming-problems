
import numpy as np

def rotate_matrix(M):
    #anticlockwise matrix rotation  
    N=len(M)
    for i in range(N//2): #number of cycles
        for j in range(i,N-1-i):          
            temp=M[i][j]
            M[i][j]=M[j][-1-i]
            M[j][-1-i]=M[-1-i][-1-j]
            M[-1-i][-1-j]=M[-1-j][i]
            M[-1-j][i]=temp            
    return M

def matrix_to_string(M):
    return ' '.join([' '.join(l) for l in M])
    

if __name__ == '__main__':
    t=int(input())

    for count in range(t):
        N=int(input())
        arr=input().split(' ')
        matrix=[arr[i*N:(i+1)*N] for i in range(N)]
        
        # print(np.array(matrix))
        # print()
        # print(np.array(rotate_matrix(matrix)))
        
        print(matrix_to_string(rotate_matrix(matrix)))