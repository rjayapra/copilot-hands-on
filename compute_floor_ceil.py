import math

def compute_floor_ceil(value):
    """
    Compute the floor and ceiling values of a given number.

    Parameters:
    value (float): The number for which to compute the floor and ceiling values.

    Returns:
    tuple: A tuple containing the floor value and the ceiling value of the input number.
    """
    floor_value = math.floor(value)
    ceil_value = math.ceil(value)
    return floor_value, ceil_value

# Example usage
value = 4.7
floor_val, ceil_val = compute_floor_ceil(value)
print(f"Floor value: {floor_val}, Ceil value: {ceil_val}")