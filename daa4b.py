# 0/1 knapsack problem using branch and bound

import heapq

def bound(level, profit, weight, w, p, capacity, n):
    if weight >= capacity:
        return profit

    result = profit
    j = level + 1
    total = weight

    while j < n and total + w[j] <= capacity:
        total += w[j]
        result += p[j]
        j += 1

    if j < n:
        result += (capacity - total) * p[j] / w[j]

    return result


def knapsack(w, p, capacity):
    n = len(w)

    items = sorted(zip(w, p), key=lambda x: x[1]/x[0], reverse=True)
    w = [x[0] for x in items]
    p = [x[1] for x in items]

    pq = []

    max_profit = 0

    b = bound(-1, 0, 0, w, p, capacity, n)
    heapq.heappush(pq, (-b, 0, 0, -1))

    while pq:
        neg_b, profit, weight, level = heapq.heappop(pq)

        if -neg_b <= max_profit:
            continue

        i = level + 1

        if i >= n:
            continue

        new_weight = weight + w[i]
        new_profit = profit + p[i]

        if new_weight <= capacity:
            max_profit = max(max_profit, new_profit)

            b = bound(i, new_profit, new_weight, w, p, capacity, n)

            if b > max_profit:
                heapq.heappush(
                    pq, (-b, new_profit, new_weight, i)
                )

        b = bound(i, profit, weight, w, p, capacity, n)

        if b > max_profit:
            heapq.heappush(pq, (-b, profit, weight, i))

    return max_profit


n = int(input("Enter number of items: "))

w = []
p = []

for i in range(n):
    w.append(int(input("Enter weight: ")))
    p.append(int(input("Enter profit: ")))

capacity = int(input("Enter knapsack capacity: "))

print("Maximum Profit:", knapsack(w, p, capacity))