def below_zero(operations: List[int]) -> bool:
    """Detect if the balance of account falls below zero at any point"""
    balance = 0
    for op in operations:
        balance -= op
        if balance < 0:
            return True
    return False