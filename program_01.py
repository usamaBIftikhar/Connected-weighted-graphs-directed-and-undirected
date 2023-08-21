from array import *
import os
import sys
from queue import PriorityQueue
from numpy import equal

class Graph:


    ##Default Constructor 
    ##Which will called Automatically
    #When the Object is Created in main Function
    #It will this intilize the Components of our Graph!
    def __init__(self, total_vertices):
        self.v = total_vertices
        self.edge = [[-1 for i in range(total_vertices)] for j in range(total_vertices)]
        
        self.visited = []  #managing Array for keeping the Records of Nodes which are visited Completely!

    #Function Which will Add Edge in our graph!
    # When This Function is Called through main 
    # by using object.  (opertor)
    # this function will get called accordingly 
    def AddEdge(self, u, v, weight):
        self.edge[u][v] = weight
        self.edge[v][u] = weight  




def Dijkstra_func(graph, init_node):

    NODE = {v:float('inf') for v in range(graph.v)}
    NODE[init_node] = 0
    


    #------Priority Queue----------------------
    #here Priority Queue will be managed !!
    #where all those nodes who will got visited once are 
    #Supposed to be in this Priority Queue
    #they will be in this until all their 
    #Adjacent Nodes are Not Visited Completely!
    visited_node_rec = PriorityQueue()

    #here first NODE Is Already Visited so we'll ignore it and
    #We will go for it's adjacent NODES

    visited_node_rec.put((0, init_node))

    while not visited_node_rec.empty():
        (dist, current_vertex) = visited_node_rec.get()

        #here The NODE Which is visited is supposed to be in
        # Priority Queue because we are supposed to use it to find
        # Find the weight of those nodes Adjacent to that node
        graph.visited.append(current_vertex)

        for adjacent_Node in range(graph.v):
            if graph.edge[current_vertex][adjacent_Node] != -1:

                #here the Distance Variable will thus Contain
                #The Distance or we can say the Path between
                #the Current NODE at which we are Currently Present
                #And the node which will be adjacent to that specific Node
                weight = graph.edge[current_vertex][adjacent_Node]


                if adjacent_Node not in graph.visited:

                    #here we'll Find the COST of that Node from it's previous Adjacent NODE
                    # For Example we are at A is starting NODE
                    # then we'll Find Distance from A --> B and it weight for example (2)
                    # then from B --> E the COST is (5)
                    # here the NEW weight is Produce in that way A ---> B ----> E (5+2)
                    # Previous_weight + Cuurent_weight

                    previous_weight = NODE[adjacent_Node]
                    current_weight = NODE[current_vertex] + weight


                    # here we will compare weight 
                    # For example is the Previous weight from A-->E is (4)
                    # But with some other Edge our current_eight is (3)
                    # so we'll assign this weight to weight of that vertex is our Graph
                    if current_weight < previous_weight:

                        visited_node_rec.put((current_weight, adjacent_Node))
                        NODE[adjacent_Node] = current_weight
    return NODE


if __name__ == "__main__":

  g = Graph
  Counter=1
  #here is the 2D Array Representing our graph!!
  #Each of the row representing each vertex
  with open('file_01.txt') as inpt:
    while True:
      data = inpt.readline() 
      if not data:
        break
      else:
        if(list(data)[0]=='*'):
          #parsing and formatting the data
          numVertices = int(data.split("=")[-1])
          g = Graph(numVertices)
          inpt.readline()
          while True:
            vertices = inpt.readline()
            if(len(vertices)>25):
              vertexData = vertices.split(",")
              vertex = vertexData[0].split("(")
              weight = vertexData[2].split(")")
              w = float(weight[0][1:])
              v = int(vertexData[1][1:])
              u = int(vertex[1])
              g.AddEdge(u, v, w)
              break
            else:
              vertexData = vertices.split(",")
              vertex = vertexData[0].split("(")
              weight = vertexData[2].split(")")
              w = float(weight[0][1:])
              v = int(vertexData[1][1:])
              u = int(vertex[1])
              g.AddEdge(u, v, w)
          
          shortest_path=Dijkstra_func(g, 0)
          print("\n\n----------------Graph :",Counter,"--------------------------\n\n")
          Counter=Counter+1
          for vertex in range(len(shortest_path)):
           print("(0 ,", vertex,shortest_path[vertex],")")
       
          
  os.system("pause")


