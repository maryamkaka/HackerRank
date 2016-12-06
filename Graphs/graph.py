class graph(object):

    #constructor
    def __init__(self, g):
        self.graph = g

    #determine a path (uses backtracking)
    def find_path(self, start, end, path=[]):
        path = path + [start]

        if(start == end):   #base case
            return path
        elif(not(start in self.graph) or not(end in self.graph)):
            return None

        for n in self.graph[start]:
            if(not(n in path)):
                newpath = self.find_path(n, end, path)
                if newpath: return newpath

        return None

    #find all paths


g = graph({'A': ['B', 'C'], 'B': ['C', 'D'], 'C': ['D'], 'D': ['C'], 'E': ['F'], 'F': ['C']})
print(g.find_path('A', 'G'))
