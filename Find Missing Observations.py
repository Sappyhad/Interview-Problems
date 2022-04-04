
def missingRolls(rolls: list[int], mean: int, n: int):
    missingSum = mean * (n + len(rolls)) - sum(rolls)
    part, rem = divmod(missingSum, n)
    ans = [part] * n
    while missingSum < n or missingSum > 6 * n:
        return []
    for i in range(rem):
        ans[i] += 1
    return ans


print(missingRolls(rolls=[3,2,4,3], mean=4, n=2))