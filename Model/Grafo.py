from math import inf


class Grafo:
    def __init__(self):
        self.graph = []
        self.n_ver = 0
        self.sedes = []

    def add_vert(self, object):
        self.n_ver += 1
        self.graph.append([0]*self.n_ver)
        self.sedes.append(object)

        if self.n_ver != 0:
            for i in range(len(self.graph)-1):
                dist = self.calc_dist(object, i)
                self.graph[i].append(dist)
                self.graph[len(self.graph[i])-1][i] = dist


    def calc_dist(self, object, index):
        return ((object.coordendas[0] - self.sedes[index].coordendas[0])**2+(object.coordendas[1] - self.sedes[index].coordendas[1])**2)**(1/2)

    def printGraph(self):
        for i in self.graph:
            print(i)

    def find_all(self, start, end=-1):
        n = self.n_ver

        dist = [inf]*n
        dist[start] = self.graph[start][start]  # 0

        spVertex = [False]*n
        parent = [-1]*n

        path = [{}]*n

        for count in range(n-1):
            minix = inf
            u = 0

            for v in range(len(spVertex)):
                if spVertex[v] == False and dist[v] <= minix:
                    minix = dist[v]
                    u = v

            spVertex[u] = True
            for v in range(n):
                if not(spVertex[v]) and self.graph[u][v] != 0 and dist[u] + self.graph[u][v] < dist[v]:
                    parent[v] = u
                    dist[v] = dist[u] + self.graph[u][v]

        for i in range(n):
            j = i
            s = []
            while parent[j] != -1:
                s.append(j)
                j = parent[j]
            s.append(start)
            path[i] = s[::-1]

        return (dist[end], path[end]) if end >= 0 else (dist, path)

    def camino_mas_corto(self, star):
        i = 0
        ruta=[]
        viajado = [False]*self.n_ver
        father = star
        while len(ruta) != self.n_ver - 1:
            shortest_path = inf
            min_index = inf
            hijos = [r for r in range(len(self.graph[father])) if self.graph[father][r] != 0 and viajado[r] != True]
            viajado[father] = True 
            for j in range(self.n_ver):
                if self.graph[father][j] < shortest_path and viajado[j] != True:
                    min_index = j
                    shortest_path = self.graph[father][j]
                
            ruta.append((father, min_index))
            father = min_index
            i+= 1

        return ruta


                 




