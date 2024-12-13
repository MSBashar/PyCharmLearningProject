def find_average(values: list[int]) -> float:
    result: int = 0
    for v in values:
        result += v
    return result / len(values)


print("Average", find_average([5, 6, 7, 8]))
