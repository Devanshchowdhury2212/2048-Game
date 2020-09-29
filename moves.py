import random
def start():
    mat=[]
    for i in range(4):
        mat.append([0]*4)
    return mat
def add_number(mat):
    x = random.randint(0,3)
    y = random.randint(0,3)
    while mat[x][y]!=0:
        x = random.randint(0,3)
        y = random.randint(0,3)
    mat[x][y]=2
def status(mat):
    for i in range(4):
        for j in range(4):
            if mat[i][j]==2048:
                return 'YOU WIN'
    for i in range(4):
        for j in range(4):
            if mat[i][j]==0:
                return 'ON'
    for i in range(3):
        for j in range(4):
            if mat[i][j]==mat[i+1][j]:
                return 'ON'
    for i in range(4):
        for j in range(3):
            if mat[i][j]==mat[i][j+1]:
                return 'ON'
    for j in range(3):
        if mat[3][j]==mat[3][j+1]:
            return 'ON'
    for i in range(3):
        if mat[i][3]==mat[i+1][3]:
            return 'ON'
    return 'GAME OVER'


def move_up(mat):
    # for i in mat:
    #     print(i)
    flag =False
    for i in range(3):
        for j in range(4):
            if mat[i][j]==mat[i+1][j]:
                mat[i][j]*=2
                flag = True
                for k in range(i+1,3):
                    mat[k][j] = mat[k+1][j]
                mat[3][j]=0 
    while 2:
        c=0
        for i in range(3):
            for j in range(4):
                if mat[i][j]==0 and mat[i+1][j]:
                    flag = True
                    mat[i+1][j],mat[i][j]=mat[i][j],mat[i+1][j]
                    c+=1
        if not c:
            break
    return mat,flag
         
                    
        

def move_down(mat):
    # for i in mat:
    #     print(i)
    flag = False
    for i in range(1,4):
        for j in range(4):
            if mat[i][j]==mat[i-1][j]:
                mat[i][j]*=2
                flag = True
                for k in range(i-1,0,-1):
                    mat[k][j] = mat[k-1][j]
                mat[0][j]=0
    while 2:
        c=0
        for i in range(1,4):
            for j in range(4):
                if mat[i][j]==0 and mat[i-1][j]:
                    flag = True
                    mat[i-1][j],mat[i][j]=mat[i][j],mat[i-1][j]
                    c+=1
        if not c:
            break
    return mat,flag
       

def move_right(mat):
    # for i in mat:
    #     print(i)
    flag = False
    for i in range(4):
        for j in range(1,4):
            if mat[i][j]==mat[i][j-1]:
                mat[i][j]*=2
                flag = True
                for k in range(j-1,0,-1):
                    mat[i][k] = mat[i][k-1]
                mat[i][0]=0
    while 2:
        c=0
        for i in range(4):
            for j in range(1,4):
                if mat[i][j]==0 and mat[i][j-1]:
                    mat[i][j],mat[i][j-1]=mat[i][j-1],mat[i][j]
                    c+=1
                    flag = True
        if not c:
            break    
    return mat,flag

def move_left(mat):
    # for i in mat:
    #     print(i)
    flag = False
    for i in range(4):
        for j in range(3):
            if mat[i][j]==mat[i][j+1]:
                mat[i][j]*=2
                flag = True
                for k in range(j+1,3):
                    mat[i][k] = mat[i][k+1]
                mat[i][3]=0
    while 2:
        c=0
        for i in range(4):
            for j in range(3):
                if mat[i][j]==0 and mat[i][j+1]:
                    flag = True
                    mat[i][j],mat[i][j+1]=mat[i][j+1],mat[i][j]
                    c+=1
        if not c:
            break 
    return mat,flag



