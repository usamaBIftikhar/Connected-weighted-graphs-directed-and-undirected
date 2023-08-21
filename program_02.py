from array import *
import sys
from queue import PriorityQueue
from numpy import equal
class Graph:

    ##Default Constructor 
    ##Which will called Automatically
    #When the Object is Created in main Function
    #It will this intilize the Components of our Graph!
    def __init__(self, vertex):
        self.total_vertex = vertex
        self.graph = []




    #Function Which will Add Edge in our graph!
    # When This Function is Called through main 
    # by using object.  (opertor)
    # this function will get called accordingly
    def AddEdge(self, temp_01, temp_02, weight):
        self.graph.append([temp_01, temp_02, weight])

        
        
 
   

 
  
    def kruskal(self):


        final_distance = []  # This Array is supposed to store the deduced
                             # results of Shortest Path of Edges and the weight

        graph_iterator=0     # This variable here is used to iterate over the graph
                             # Like the graph is being iterated when this variable got incremented in loop

        count_check = 0


        self.graph = sorted(self.graph, key=lambda item: item[2])


        adjacents = []
        pos = []
        
        for node in range(self.total_vertex):
            adjacents.append(node)
            pos.append(0)


        # Here this following loop will be ended when the first shortest path is being 
        # deduced by us and after this the next point 
        # will be discoverd after that
        while count_check < self.total_vertex - 1:
            edge_01, edge_02, w = self.graph[graph_iterator]
            graph_iterator = graph_iterator + 1


            temp_01 = self.check_adjacents(adjacents, edge_01)
            temp_02 = self.check_adjacents(adjacents, edge_02)


            if temp_01 != temp_02:
                count_check = count_check + 1
                final_distance.append([edge_01, edge_02, w])
                self.checkUnion(adjacents, pos, temp_01, temp_02)

        # here making the total Weight ZERO because
        # when shortest path from A --> E is fianlly set
        # then making the total_weight variable to zero
        # because it is in loop and the next weight is 
        # supposed to be start from ZERO        
        total=0        


        #here printing the final results 
        # Which comprises information about our edges and total weight
        # Which was being stored in our result list 
        for edge_01, edge_02, total_weight in final_distance:

            print("(", edge_01," ", edge_02, " ", total_weight,")")
            total=total+total_weight

        # here total Weight is being printed Outside our loop
        # which was calculated in our above for loop 
        # while pritning answers    
        print("Total Weight =", total)
        print("\n----------------------\n")


     # This Function is usedd to Check the Adjacents of Graph
    # Like Suppose if B and C are adjecnt to A
    # then they are supposed to return i
    def check_adjacents(self, adjacent, i):
        if adjacent[i] == i:
            return i
        return self.check_adjacents(adjacent, adjacent[i])


    # Here this Function is Supposed to Calculate 
    # Union of two Edges 
    # Like two edges passed in this Function
    # Like temp_01 and temp_02 are both edges passed into it
    def checkUnion(self, adjacent, pos, temp_01, temp_02):

        
        #here the Function is called the edge that was passed in
        # checkUnion function are thus passed to check_adjacents function
        # and there results are comapred on the bases of their adjacents!
        temp_node_01 = self.check_adjacents(adjacent, temp_01)
        temp_node_02 = self.check_adjacents(adjacent, temp_02)

        
        if pos[temp_node_01] < pos[temp_node_02]:
            adjacent[temp_node_01] = temp_node_02


        elif pos[temp_node_01] > pos[temp_node_02]:
            adjacent[temp_node_02] = temp_node_01


        else:
            adjacent[temp_node_02] = temp_node_01
            pos[temp_node_01] += 1


if __name__ == "__main__":

  g = Graph
  Counter=1
  #here is the 2D Array Representing our graph!!
  #Each of the row representing each vertex
  with open('file_02.txt') as inpt:
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
          
          print("\nMinimum Spanning tree\n")
          g.kruskal()
        
       