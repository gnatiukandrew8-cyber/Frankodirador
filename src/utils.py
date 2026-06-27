"""
Utility functions for Frankodirador application.
"""


def add(a: int, b: int) -> int:
    """
    Add two numbers.
    
    Args:
        a: First number
        b: Second number
        
    Returns:
        int: Sum of a and b
    """
    return a + b


def subtract(a: int, b: int) -> int:
    """
    Subtract two numbers.
    
    Args:
        a: First number
        b: Second number
        
    Returns:
        int: Difference of a and b
    """
    return a - b


def multiply(a: int, b: int) -> int:
    """
    Multiply two numbers.
    
    Args:
        a: First number
        b: Second number
        
    Returns:
        int: Product of a and b
    """
    return a * b


def divide(a: int, b: int) -> float:
    """
    Divide two numbers.
    
    Args:
        a: Dividend
        b: Divisor
        
    Returns:
        float: Result of division
        
    Raises:
        ValueError: If divisor is zero
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
