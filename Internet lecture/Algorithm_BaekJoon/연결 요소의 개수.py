import sys
input = sys.stdin.readline

def find_parent(parent, a):
    if parent[a] != a:
        parent[a] = find_parent(parent, parent[a])
    return parent[a]

def union_parent(parent, a, b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a<b :
        parent[b]= a
    else :
        parent[a] = b

n, m = map(int, input().split())
parent = [0] * (n+1)

for i in range(1,n+1):
    parent[i] = i

for i in range(m):
    a,b = map(int, input().split())
    union_parent(parent, a, b)

counter = set()
for i in range(1,n+1):
    print(find_parent(parent,i))
    counter.add(find_parent(parent,i))

print(len(counter))

