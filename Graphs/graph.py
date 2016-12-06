class graph(object):

    #constructor
    def __init__(self, g):
        self.graph = g

    #string representation of graph
    def __str__(self):
        s = ''

        for n in self.graph:
            for x in self.graph[n]:
                s += n + '->' + x + '\n'

        return s

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
    def find_all_paths(self, start, end, path=[]):
        path = path + [start]

        if(start == end):   #base case
            return path
        elif(not(start in self.graph) or not(end in self.graph)):
            return None

        paths = []
        for n in self.graph[start]:
            if(not(n in path)):
                newpaths = self.find_all_paths(n, end, path)
                paths.append(newpaths)
        return paths


g = graph({'A': ['B', 'C'], 'B': ['C', 'D'], 'C': ['D'], 'D': ['C'], 'E': ['F'], 'F': ['C']})
print(g)
print(g.find_all_paths('A', 'C'))
