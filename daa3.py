def fractional_knapsack(w,p,capacity):
    n = len(w)
    ratio = []

    for i in range(n):
        ratio.append((p[i]/w[i],w[i],p[i]))

    ratio.sort(reverse=True)

    total_profit = 0

    for r,weight,profit in ratio:
        if capacity >= weight:
           capacity -= weight
           total_profit += profit
        else:
            total_profit += r*capacity
            break

    return total_profit


n = int(input("enter number of items:"))

w = []
p = []

for i in range(n):
    weight = int(input("enter weight:"))
    profit = int(input("enter profit:"))
    w.append(weight)
    p.append(profit)

capacity = int(input("enter knapsack capacity:"))
print("maximum profit:",fractional_knapsack(w,p,capacity))
