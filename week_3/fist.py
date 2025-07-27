
# create a binary tree and calculate the hieght


# class Node:
#     def __init__(self,value):
#         self.value = value
#         self.left = None
#         self.right = None
    


# def height(root):
#     if root is None:
#         return - 1
#     left_height = height(root.left)
#     right_height = height(root.right)
#     return 1 + max(left_height,right_height)



# root = Node(1)

# root.left = Node(2)

# root.right = Node(3)

# root.left.left = Node(4)

# root.right.right = Node(5)


# print("hiegth: ",height(root))


# create max heap and insert element into max heap and display it

# class MaxHeap:
#     def __init__(self):
#         self.heap = []
    
#     def insert(self,value):
#         self.heap.append(value)
#         self._heapify_(len(self.heap)-1)
    
#     def _heapify_(self,index):
#         parent = (index-1 ) // 2

#         if index > 0 and self.heap[index] > self.heap[parent]:
#             self.heap[ index],self.heap[parent] = self.heap[parent], self.heap[index]
#             self._heapify_(parent)
    
#     def display(self):
#         print(self.heap)

 


# heap = MaxHeap()

# heap.insert(10)
# heap.insert(20)
# heap.insert(50)
# heap.insert(15)

# heap.display()


# graph = {
#     'A': ['B', 'C'],
#     'B': ['A', 'D', 'E'],
#     'C': ['A', 'F'],
#     'D': ['B'],
#     'E': ['B', 'F'],
#     'F': ['C', 'E']
# }

# dfs traversal

class Graph:
    def __init__(self,vertices):
        self.v = vertices
        self.graph = [[] for _ in range (vertices)]

    
    def add_edge(self,u, v):
        self.graph[u].append(v)
    
    def dfs_u(self,v, visited):
        visited[v]= True
        print(v,end=' ')
        for nibor in self.graph[v]:
            if not visited[nibor]:
                self.dfs_u(nibor,visited)
    

    def dfs(self,start):
        visited = [False] * self.v

        self.dfs_u(start,visited)


g= Graph('A')

g.add_edge('B','')