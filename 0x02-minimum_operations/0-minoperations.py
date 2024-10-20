def minOperations(n):
    if n <= 1:
        return 0

    operations = 0

    for i in range(2, n + 1):
        while n % i == 0:
            operations += i  # Add i for "Copy All" + "Paste"
            n //= i          # Reduce n
    return operations
