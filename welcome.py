def find_average(values: list[int]) -> str:
    result: int = 0

    for v in values:
        result += v
    return result / len(values)

print("AVERAGE", find_average([5,6, 7, 8]))
