def main(a):
    """
    Given an integer a, check the following conditions:
    "two-digit odd number",
    "two-digit even number",
    "three-digit odd number",
    "three-digit even number"

    Args:
        a: integer
    Returns:
        string: the message to print
    """
    p = a//100
    if p==0:
        if a%2==0:
            return "two-digit even number"
        if a%2!=0:
            return "two-digit odd number"
    if p > 0 :
        if a%2==0:
            return "three-digit even number"
        if a%2!=0:
            return "three-digit odd number"
print(main(a=133))
        