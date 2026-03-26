# 그래프, DFS, BFS - DFS와 BFS (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/1260
from collections import deque

# 아이디어: 그냥 그래프 주어지면 bfs, dbs 탐색한 결과 출력하는거, 방문할수 있는 정점이 여러개일때는 작은거부터 sort()

# 함수 bfs(): bfs로 탐색하는 함수, dbf(): dbf로 탐색하는 함수

# O(E log v) = 10^5 < 2*(10^8)


# 입력:
# 1. 정점의개수, 간선의개수, 시작할 정점의 번호
# 2. 간선이 연결하는 두 정점의 번호
#
# 출력:
# dbs로 탐색한 결과
# bfs로 탐색한 결과
# 4 5 1
# 1 2
# 1 3
# 1 4
# 2 4
# 3 4

vertex, edge, start = map(int,input().split())

graph = {i:[] for i in range(1, vertex+1)}
for i in range(edge):
    u, v = map(int, input().split())

    graph[u].append(v)
    graph[v].append(u)

def dfs():

    stack = [start]
    visited_stack = []
    while stack:
        pop_node = stack.pop()

        if not pop_node in visited_stack:
            visited_stack.append(pop_node)

            for neighbor in sorted(graph[pop_node], reverse=True):
                    stack.append(neighbor)

    return visited_stack


def bfs():

    queue = deque([start])
    visited_queue = [start]
    while queue:

        popleft_node = queue.popleft()
        # print("뺸값", popleft_node)

        for neighbor in (graph[popleft_node]):
            if not neighbor in visited_queue:
                queue.append(neighbor)
                visited_queue.append(neighbor)
                # print("넣은값", neighbor)

    return visited_queue





print(*dfs())
print(*bfs())









