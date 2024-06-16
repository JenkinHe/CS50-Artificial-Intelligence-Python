import sys

class Node():
    def __init__(self,state,parent,action):
        self.state=state
        self.parent = parent
        self.action = action

class StackFrontier():
    def __init__(self):
        self.frontier =[]

    def add(self,node):
        self.frontier.append(node)

    def contains_state(self,state):
        return any(node.state== state for node in self.frontier)
    
    def empty(self):
        return len(self.frontier)==0
    
    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node= self.frontier[-1]
            self.frontier = self.frontier[:-1]
            return node
        
class QueueFrontier(StackFrontier):

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node =self.frontier[0]
            self.frontier = self.frontier[1:]
            return node
        

class Maze():

    def __init__(self,filename):

        #Read file and set height and width of maze 
        with open(filename) as f:
            contents=f.read()
        
        # Validate start and goal
        if contents.count("A")!=1:
            raise Exception("maze must have exactly one start point")
        if contents.count("B")!=1:
            raise Exception("maze must have exactly one goal ")
        
        # Determine height and width of maze
        contents = contents.splitlines()
        self.height=len(contents)
        self.width = max(len(line) for line in contents)

        # Keep track of walls
        self.walls =[]
        for i in range(self.height):
            row=[]
            for j in range(self.width ):
                try:
                    if contents[i][j]=="A":
                        self.start=(i,j)
                        row.append(False)
                    elif contents[i][j]=="B":
                        self.goal=(i,j)
                        row.append(False)
                    elif contents[i][j]==" ":
                        row.append(False)
                    else:
                        row.append(True)
                except IndexError:
                    row.append(False)
            self.walls.append(row)
        
        self.solution=None


def solve(self):
    """ Finds a solution to maze, if one exists"""

    # Keep track of number of states explored
    self.num_explored=0

    # initialise frontier to just the starting position
    start= Node(state=self.start, parent=None,action=None)
    frontier =StackFrontier()
    frontier.add(start)

    # Initialise an empty explored set
    self.explored=set()

    # Keep looping until solution found
    while True:

        # if nothing left in frontier then no path
        if frontier.empty():
            raise Exception("no solution")
        
        node = frontier.remove()
        self.num_explored+=1

        if node.state == self.goal:
            actions=[]
            cells= []

            # Follow parent nodes to find solution

            while node.parent is not None:
                actions.append(node.action)
                cells.append(node.state)
                node=node.parent
            actions.reverse()
            cells.reverse()
            self.solution=(actions,cells)
            return
        
        # mark node as explored
        self.explored.add(node.state)

        # add neighbours to frontier
        for action,state in self.neighbors(node,state):
            if not frontier.contains_state(state) and state not in self.explored:
                child = Node(state=state,parent=node,action=action)
                frontier.add(child)
