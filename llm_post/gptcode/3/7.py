def below_zero(operations: List[int]) -> bool:
    balance = 0  # initialize balance to zero
    for operation in operations:
        balance += operation  # add the operation to the balance
        if balance < 0:  # check if balance falls below zero
            return True
    return False