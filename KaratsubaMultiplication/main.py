import math

def number_of_digits(number: int) -> int:
    return int(math.log10(abs(number))) + 1

def multiply(x: int, y: int) -> int:
    # We CAN multiply small numbers
    if abs(x) < 10 or abs(y) < 10:
        return x * y

    # Calculate the size of the numbers
    digits = max(number_of_digits(x), number_of_digits(y))
    midpoint = 10 ** (digits // 2)

    # Split digit sequences in the middle
    high_x = x // midpoint
    low_x = x % midpoint
    high_y = y // midpoint
    low_y = y % midpoint

    # 3 recursive calls to numbers approximately half the size
    z0 = multiply(low_x, low_y)
    z1 = multiply(low_x + high_x, low_y + high_y)
    z2 = multiply(high_x, high_y)

    return (z2 * midpoint**2) + ((z1 - z2 - z0) * midpoint) + (z0)

print(multiply(3141592653589793238462643383279502884197169399375105820974944592,2718281828459045235360287471352662497757247093699959574966967627))