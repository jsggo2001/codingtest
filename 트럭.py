from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    count = 0
    all_weight = 0
    brige = [0] * bridge_length
    truck_weights = deque(truck_weights)
    while len(truck_weights) != 0 or count != 0:
        # 다리 위에 트럭 이동
        for i in range(len(brige) - 1, -1, -1):
            if brige[i] != 0:
                if i == len(brige) - 1:
                    all_weight = all_weight - brige[i]
                    brige[i] = 0
                    count -= 1
                else:
                    brige[i + 1] = brige[i]
                    brige[i] = 0
        if len(truck_weights) != 0:
            next = truck_weights[0]
            # 트럭이 올라갔을때 다리에 하중 계산후 낮으면 다리에 올리기
            if all_weight + next <= weight:
                truck_weights.popleft()
                if brige[0] == 0:
                    brige[0] = next
                    all_weight = all_weight + next
                    count += 1

        answer += 1

    return answer


print(solution(2, 10, [7, 4, 5, 6]))
print(solution(100, 100, [10]))
print(solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]))
