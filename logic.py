from functions import *
end=readend()
start=readstart()
print("number 1 = bfs algorithm")
print("number 2 = dfs algorithm")
print("number 3 = ids algorithm")
print("number 4 = A* algorithm")
selector=int(input("select one of them"))
if selector==1:
    print("waiting...")
    starttime=time.time()
    soloution=bfs(start,end)
    endtime=time.time()
if selector==2:
    print("waiting...")
    starttime = time.time()
    limit=int(input("enter depth limit"))
    soloution=dfs(start,end,limit)
    endtime = time.time()
if selector==3:
    print("waiting...")
    starttime = time.time()
    limit = int(input("enter depth limit"))
    soloution=ids(start,end,limit)
    endtime = time.time()
if selector==4:
    print("waiting...")
    starttime = time.time()
    soloution=astar(start,end)
    endtime = time.time()


show_state(start)
counter=0
print('--------------------')
while True:
    if soloution[counter]==end:
        break
    show_state(soloution[counter])
    print('--------------------')
    counter+=1
show_state(end)
print("time:"+str(endtime-starttime))