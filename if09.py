def main(a):
    """
    The two-digit integer is given.
    Replace the digits of the number.
    True if the resulting number is less than or equal to the old number, otherwise return False.
    
    Args:
        a: integer
    Returns:
        boolean: True if the resulting number is less than or equal to the old number, otherwise return False.
    """

    x = (a%10)*10
    y = a//10
    ans = x+y
    if ans <= a:
        return True
    if ans >= a:
        return False
print(main(a=93))