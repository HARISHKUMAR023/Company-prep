def fib(n):
    # Base cases
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        # Recursive case: sum of the two preceding numbers
        return fib(n - 1) + fib(n - 2)

print(fib(6))

