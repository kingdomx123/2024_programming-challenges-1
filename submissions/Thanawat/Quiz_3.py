import heapq
from collections import defaultdict

def Dijkstra_Algorithm (edges, start, end):
    graph = defaultdict(list)
    for u, v, weight in edges:
        graph[u].append((weight, v))
        graph[v].append((weight, u))

    heap = [(0, start)]
    visited = set()
    min_distances = {start: 0}

    while heap:
        current_distance, current_node = heapq.heappop(heap)

        if current_node == end:
            return current_distance

        if current_node in visited:
            continue

        visited.add(current_node)

        for weight, neighbor in graph[current_node]:
            distance = current_distance + weight
            if neighbor not in min_distances or distance < min_distances[neighbor]:
                min_distances[neighbor] = distance
                heapq.heappush(heap, (distance, neighbor))

    return float('inf')  


edges = []
num_edges = int(input("กรุณากรอกจำนวน edges ที่ต้องการ: "))

for i in range(num_edges):
    u, v, weight = map(int, input(f"กรุณากรอก edge ที่ {i+1} (รูปแบบในการกรอกข้อมูล: จุดเริ่มต้น จุดสิ้นสุด น้ำหนัก): ").split())
    edges.append((u, v, weight))

start = int(input("กรุณากรอกจุดเริ่มต้น: "))
end = int(input("กรุณากรอกจุดสิ้นสุด: "))


shortest_path_length = Dijkstra_Algorithm(edges, start, end)
print(f"ความยาวของเส้นทางที่สั้นที่สุดจาก {start} ไป {end} คือ {shortest_path_length}")
