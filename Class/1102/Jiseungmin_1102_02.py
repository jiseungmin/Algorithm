# 제목:  위상 정렬
# 작성자 : 컴퓨터 공학부 지승민
# 작성일 : 2023.11.02

def topological_sort(graph):
  inDeg = {}
  for v in graph:
    inDeg[v] = 0
  for v in graph:
    for u in graph[v]:
      inDeg[u] += 1
  
  visit = []
  for v in graph :
    if inDeg[v] == 0 :
      visit.append(v)
  
  while visit :
    v = visit.pop()
    print(v, end=' ')

    for u in graph[v]:
      inDeg[u] -= 1
      if inDeg[u] == 0:
        visit.append(u)

mygraph = {"A":{"C","D"},
           "B":{"D","E"},
           "C":{"D","F"},
           "D": {"F"},
           "E": {"F"},
           "F": set()
           }

print('topological_sort: ')
topological_sort(mygraph)
print()
