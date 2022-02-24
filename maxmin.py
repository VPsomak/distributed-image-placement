def max_min_fairness(demands, capacity):
    capacity_remaining = capacity
    output = []

    for i, demand in enumerate(demands):
        share = capacity_remaining / (len(demands) - i)
        allocation = min(share, demand)

        if i == len(demands) - 1:
            allocation = max(share, capacity_remaining)

        output.append(allocation)
        capacity_remaining -= allocation

    return output


# tests = [
#     (dict(demands=[1, 1], capacity=20), [1, 19]),
#     (dict(demands=[2, 8], capacity=10), [2, 8]),
#     (dict(demands=[2, 8], capacity=5), [2, 3]),
#     (dict(demands=[1, 2, 5, 10], capacity=20), [1, 2, 5, 12]),
#     (dict(demands=[2, 2.6, 4, 5], capacity=10), [2, 2.6, 2.7, 2.7]),
# ]

output  = max_min_fairness(demands=[1, 2, 5, 10], capacity=20)
print("max-min fairnes", output)