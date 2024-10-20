#!/usr/bin/python3
"""
0-minoperations.py
"""


def minOperations(n):
    """Minimum operations algorithm"""
    if n <= 1:
        return 0

    operations = 0

    for i in range(2, n + 1):
        while n % i == 0:
            operations += i
            n //= i
            return operations
