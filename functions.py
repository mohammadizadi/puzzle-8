from classes import *
import time
def readstart():
    f = open("start.txt", "r")
    start=[]
    for line in f:
        start.append(line.rstrip('\n'))
    return start


def readend():
    f = open("end.txt", "r")
    end=[]
    for line in f:
        end.append(line.rstrip('\n'))
    return end



def show_state(state):
    print(state[0]+'    '+state[1]+'    '+state[2])
    print(state[3]+'    '+state[4]+'    '+state[5])
    print(state[6]+'    '+state[7]+'    '+state[8])



def move_up(state):
    temp_state=state[:]
    index=temp_state.index('*')
    if index not in [0,1,2]:
        temp=temp_state[index-3]
        temp_state[index-3]=temp_state[index]
        temp_state[index]=temp
        return temp_state
    else:
        return None


def move_down(state):
    temp_state=state[:]
    index=temp_state.index('*')
    if index not in [6,7,8]:
        temp=temp_state[index+3]
        temp_state[index+3]=temp_state[index]
        temp_state[index]=temp
        return temp_state
    else:
        return None

def move_right(state):
    temp_state = state[:]
    index=temp_state.index('*')
    if index not in [2,5,8]:
        temp=temp_state[index+1]
        temp_state[index+1]=temp_state[index]
        temp_state[index]=temp
        return temp_state
    else:
        return None



def move_left(state):
    temp_state = state[:]
    index=temp_state.index('*')
    if index not in [0,3,6]:
        temp=temp_state[index-1]
        temp_state[index-1]=temp_state[index]
        temp_state[index]=temp
        return temp_state
    else:
        return None




def add_node(state,parent,depth,operator):
    return Node(state,parent,depth,operator)


def expand_node(node):
    childs=[]
    childs.append(add_node(move_up(node.state),node,node.depth+1,"up"))
    childs.append(add_node(move_down(node.state),node,node.depth+1,"down"))
    childs.append(add_node(move_left(node.state),node,node.depth+1,"left"))
    childs.append(add_node(move_right(node.state),node,node.depth+1,"right"))
    childs = [node for node in childs if node.state != None]
    return childs


def bfs(start,end):
    tree=[]
    tree.append(add_node(start,None,0,None))
    flag=True
    while flag:
        if len(tree)==0:
            return None
        current_node=tree.pop(0)
        if current_node.state==end:
            moves=[]
            moves_state=[]
            temp=current_node
            flag2=True
            while flag2:
                moves.insert(0,temp.operator)
                moves_state.insert(0,temp.state)
                if temp.depth==1:
                    break
                temp=temp.parent
            return moves_state
        tree.extend(expand_node(current_node))




def dfs(start,end,limit):
    tree = []
    tree.append(add_node(start, None, 0, None))
    flag = True
    while flag:
        if len(tree) == 0:
            return None
        current_node = tree.pop()
        if current_node.state == end:
            moves = []
            moves_state = []
            temp = current_node
            flag2 = True
            while flag2:
                moves.insert(0, temp.operator)
                moves_state.insert(0, temp.state)
                if temp.depth == 1:
                    break
                temp = temp.parent
            return moves_state
        if current_node.depth<=limit:
            stack=[]
            stack=expand_node(current_node)
            stack.extend(tree)
            tree=stack


def ids(start,end,limit):
    for counter in range(0,limit):
        res=dfs(start,end,counter)
        if res!=None:
            return res




def h(state):
    end={'1': [0, 0], '2': [0, 1], '3': [0, 2], '4': [1, 0], '5': [1, 1], '6': [1, 2], '7': [2, 0], '8': [2, 1]}
    h=0
    current_state={}
    raw=0
    col=0
    for counter in end:
        p=state.index(counter)
        if p in [0,1,2]:
            raw=0
        elif p in [3,4,5]:
            raw=1
        else:
            raw=2
        col=p%3
        current_state[counter]=[raw,col]
    for index in end:
        h+=abs(end[index][0]-current_state[index][0])+abs(end[index][1]-current_state[index][1])
    return h



def fn(a):
    result=(a.depth+h(a.state))
    a.fn=result
    return result

def astar(start,end):
    tree=[]
    tree.append(add_node(start,None,0,None))
    flag=True
    while flag:
        if len(tree) == 0:
            return None
        if tree[0].fn==-1:
            minfn = fn(tree[0])
        else:
            minfn=tree[0].fn
        for counter in range(1,len(tree)):
            if tree[counter].fn == -1:
                if minfn > fn(tree[counter]):
                    tree[counter],tree[0] = tree[0],tree[counter]
            else:
                if minfn > tree[counter].fn:
                    tree[counter],tree[0] = tree[0],tree[counter]
        current_node=tree.pop(0)
        if current_node.state==end:
            moves=[]
            moves_state = []
            temp=current_node
            flag2=True
            while flag2:
                moves_state.insert(0, temp.state)
                moves.insert(0,temp.operator)
                if temp.depth<=1:
                    break
                temp=temp.parent
            return moves_state
        tree.extend(expand_node(current_node))