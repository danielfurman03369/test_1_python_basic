# Quiz ID: Z75101

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


lst = [3,1,4,1,5]
print(find_median(lst))