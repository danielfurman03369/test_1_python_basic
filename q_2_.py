
def find_median(number: list) -> float:
    number.sort()
    if len(number) % 2 == 0:
        length = len(number)
        a = number[length // 2]
        b = number[(length // 2) - 1]
        median = (a + b) / 2
        return float(median)
    else:
        return float(number[len(number) // 2])



print(find_median([3,1,4,1,5]))