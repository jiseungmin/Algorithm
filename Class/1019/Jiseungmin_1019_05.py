# 제목:  그래프 BFS
# 작성자 : 컴퓨터 공학부 지승민
# 작성일 : 2023.10.19

import queue

def bfs(graph, start):
      visited = {start}
      que = queue.Queue()
      que.put(start)
      while not que.empty():
            v = que.get()
            print(v, end=' ')
            nbr = graph[v] - visited
            for u in nbr :
                  visited.add(u)
                  que.put(u)

mygraph = {"A":{"B","C"},
           "B":{"A","D"},
           "C":{"A","D","E"},
           "D":{"B","C","F"},
           "E":{"C","G","H"},
           "F":{"D"},
           "G":{"E","H"},
           "H":{"E","G"}}

print("BFS :", end='')
bfs(mygraph, "A")
print()






