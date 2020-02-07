def list_squared(m, n):
    import math
    result = []
    for number in range(m, n+1):
        sum_of_squared = 0
        for i in range(1, int(math.sqrt(number)+1)):
            if number % i == 0:
                sum_of_squared += i * i
                if number // i != i:
                    sum_of_squared += (number // i) * (number // i)
        root = math.sqrt(sum_of_squared)
        if root == int(root):
            result.append([number, sum_of_squared])
    return result
