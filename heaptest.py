import heapq
import time

# 1 * 10 5승
iterable = [1, 3, 5, 7, 4, 6] * int(1e6)

start = time.time()


def heapsort(iterrable):
    h = []
    result = []
    # 힙(h)에 삽입
    # for value in iterable:
    #     heapq.heappush(h, value)
    # 배열 자체를 힙구조로 만드는것 배열 원소를 하나씩 넣는것보다 효과적임
    heapq.heapify(iterrable)
    # 힙(h)에 모든 원소 꺼내기
    result1 = heapq.heappop(iterrable)
    # for i in range(len(h)):
    #     result.append(heapq.heappop(h))
    return result1

print(heapsort(iterable))
# print(heapsort(iterable))

end = time.time()
print(end - start)

start2 = time.time()
iterable.sort()
print(iterable[0])
end2 = time.time()
print(end2 - start2)
