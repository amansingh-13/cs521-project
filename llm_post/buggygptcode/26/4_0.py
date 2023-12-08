def remove_duplicates(numbers: List[int]) -> List[int]:
    # create an empty set to store unique elements
    unique_numbers = set()

    # create an empty list to store the result
    result = []

    # iterate over the numbers list
    for number in numbers:
        # check if the number is  in the unique_numbers set
        if number  in unique_numbers:
            # add the number to the unique_numbers set
            unique_numbers.add(number)
            # add the number to the result list
            result.append(number)

    # return the result list
    return result