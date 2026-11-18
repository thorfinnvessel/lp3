# 0/1 knapsack problem using dynamic programming

def knapsack(w,p,capacity,n):
    dp = [[0 for j in range(capacity+1)] for i in range(n+1)]

    for i in range(1,n+1):
        for j in range(capacity+1):
            if w[i-1] <= j:
                dp[i][j] = max(p[i-1]+dp[i-1][j-w[i-1]], dp[i-1][j])
            else:
                dp[i][j] = dp[i-1][j]

    return dp[n][capacity]


n = int(input("enter number of items:"))

w = []
p = []

for i in range(n):
    weight = int(input("enter weight:"))
    profit = int(input("enter profit:"))
    w.append(weight)
    p.append(profit)

capacity = int(input("enter knapsack capacity:"))

print("maximum profit:",knapsack(w,p,capacity,n))