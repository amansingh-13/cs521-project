def sort_even(l: list):
    even_indices = [i for i in range(len(l)) if i % 2 == 0]
    even_values = [l[i] for i in even_indices]
    sorted_even_values = sorted(even_values)

    result = []
    for i in range(len(l)):
        if i % 2 == 0:
            result.append(sorted_even_values.pop(0))
        else:
            result.append(l[i])

    return result