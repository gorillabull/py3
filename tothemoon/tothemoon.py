
l = [(1,2),(2,3)]
print(l[0][0])

for r in l:
    for x in r:
        print(x)

g = {
    0:{1:2, 2:4},
    1:{},
    2:{3:4,4:30},
    }

print("----------")
print(g[0][1])


a = [1, 2, 4]
b = a[:]
b.insert(2, 3)

print("-----------")

 

dictionary = dict()
 
if not(str(5) in dictionary):
    dictionary[str(5)] = []
else:
    dictionary[str(5)].append(1234) 


print(dictionary["5"])


print("-----------")

visited = [False for x in range(10000)] #replace 10k with n or smthn
def dfs(s, list):
    visited[s] = True
    for x in range(0,list[str(s)].__len__(),1):
        if visited[list[str(s)][x]] == False:
            dfs(list[str(s)][x],list)

ct = 0
lst = []
#iterative dfs
def test():
    for x in range(1,100,1):
        if visited[x] == False:
            dfs(x,lst)




def journeyToMoon(N, astronaut):
    ll = dict()
    visited = [False for x in range(10 ** 6)]  
    nodeCt= 0


    #convert double array to adjacency list
    for n in astronaut:
        if not(str(n[0]) in ll):
            ll[str(n[0])] = []
            ll[str(n[0])].append(n[1])
            if not (str(n[1]) in ll):
                ll[str(n[1])] = []
                ll[str(n[1])].append(n[1])
            else:
                ll[str(n[1])].append(n[1])
        else:
            ll[str(n[0])].append(n[1])
    
    def dfs(s, list, ccc):
        if visited[s] == False:
            ccc= ccc+1 

        visited[s] = True
        if str(s    ) in ll :
            for x in range(0,list[str(s)].__len__(),1):
                if visited[list[str(s)][x]] == False:
                    print(list[str(s)][x])
                    var = dfs(list[str(s)][x],list, ccc)
                    if var !=None:
                        ccc = ccc + var 
                    else:
                        return ccc 

    ct = 0
    perTreeNodes =[]
    i = 0
    
    #count number of nodes in each tree
    for x in range(0,N+1):
        perTreeNodes.append([])
        if visited[x] == False:
            i=  dfs(x,ll,0)
            perTreeNodes[ct] = i
            i = 0 
            ct = ct + 1 
    sum = 0 
    result = 0 
    for x in perTreeNodes:
        result = result + sum * x
        sum = sum + x 
    
    return result 

def main():
    np = input().split()

    n = int(np[0])

    p = int(np[1])

    astronaut = []

    for _ in range(p):
        astronaut.append(list(map(int, input().rstrip().split())))

    result = journeyToMoon(n, astronaut)



# Python program to print DFS traversal for complete graph 
from collections import defaultdict 
  
# This class represents a directed graph using adjacency 
# list representation 
class Graph: 
  
    P_visited =[False for x in range(10**6)]
    # Constructor 
    def __init__(self): 
  
        # default dictionary to store graph 
        self.graph = defaultdict(list) 
  
    # function to add an edge to graph 
    def addEdge(self,u,v): 
        self.graph[u].append(v) 
  
    # A function used by DFS 
    def DFSUtil(self, v, visited): 
  
        # Mark the current node as visited and print it 
        visited[v]= True
        self.P_visited[v]=True;
        print (v)
  
        # Recur for all the vertices adjacent to 
        # this vertex 
        for i in self.graph[v]: 
            if visited[i] == False: 
                self.DFSUtil(i, visited) 
  
  
    # The function to do DFS traversal. It uses 
    # recursive DFSUtil() 
    def DFS(self): 
        V = len(self.graph)  #total vertices 
  
        # Mark all the vertices as not visited 
        visited =[False]*(V) 
        
        # Call the recursive helper function to print 
        # DFS traversal starting from all vertices one 
        # by one 
        for i in range(V): 
            if visited[i] == False: 
                self.DFSUtil(i, visited) 
  
  
# Driver code 
# Create a graph given in the above diagram 
g = Graph() 
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(1, 2) 
g.addEdge(2, 0) 
g.addEdge(2, 3) 
g.addEdge(3, 3) 
  
print ("Following is Depth First Traversal")
ct = 0
for x in range(0,6):
    if g.P_visited[x] ==False:
        g.DFS() 
        ct = ct + 1 
        
print("----------------------")
print(ct)
  
# This code is contributed by Neelam Yadav 