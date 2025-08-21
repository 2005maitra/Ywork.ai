def candies(rating):
    n = len(rating)
    if n == 0:
        return 0

    candies = [1] * n

    for i in range(1, n):
        if rating[i] > rating[i - 1]:
            candies[i] = candies[i - 1] + 1

    for i in range(n - 2, -1, -1):
        if rating[i] > rating[i + 1]:
            candies[i] = max(candies[i], candies[i + 1] + 1)

    return sum(candies)


print(candies([0, 0, 0])) 