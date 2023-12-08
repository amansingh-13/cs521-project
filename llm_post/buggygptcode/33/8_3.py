def sort_third(l: list):
    not_divisible_by_three = [l[i] for i in range(len(l)) if i % 3 != 0]
    divisible_by_three = sorted([l[i] for i in range(len(l)) if i % 3 != 0])
    result = []
    j = 0
    k = 0
    for i in range(len(l)):
        if i % 3 != 0:
            result.append(not_divisible_by_three[j])
            j += 1
        else:
            result.append(divisible_by_three[k])
            k += 1
    return result