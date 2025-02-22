import math
    
def calc_precision(number: float) -> int:
    """Calculates the precision (number of decimal places) of a float number.
    :param number: The float number to calculate the precision for.
    :return: The number of decimal places.
    """
    # Keep only the decimal part of the number
    if number >= 1:
        number = float(str(number).split('.')[1])

    if number == 0:
        return 0

    # Calculate the precision
    precision = math.ceil(abs(math.log10(abs(number))))

    # Check if the precision is correct
    rest = (number * 10 ** precision) % 1
    while rest != 0:
        precision += 1
        rest = (number * 10 ** precision) % 1

    return precision

def round_step_size(quantity, step_size) -> float:
    """Rounds a given quantity to a specific step size
    :param quantity: required
    :param step_size: required
    :return: decimal
    """
    precision: int = calc_precision(step_size)
    return float(round(quantity, precision))

if __name__ == "__main__":

    print(0.0001, calc_precision(0.0001))
    print(0.0000152, calc_precision(0.0000152))
    print(10.0, calc_precision(10.0))
    print(10.2, calc_precision(10.2))
    print(9.4, calc_precision(9.4))
    print(0.0, calc_precision(0.0))