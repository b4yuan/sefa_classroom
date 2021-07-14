import re


def calculate_equation(equation):
    """
    takes a string equation and calculates the value

    :param equation: equation to calculate the grade from
    :type equation: str
    :return: float
    """

    parenthesis = re.compile(r'\([0-9.+\-*/^\s]+\)')

    for match in parenthesis.finditer(equation):
        replace = match.group(0)[1:-1]
        equation = equation.replace(match.group(0), str(calculate_equation(replace)))


    exponent = re.compile(r'(\d+\.?\d*)+\s*\^\s*(\d+\.?\d*)+')

    for match in exponent.finditer(equation):
        equation = equation.replace(str(match.group(0)), f'{float(match.group(1)) ** float(match.group(2))}')

    multdiv = re.compile(r'(\d+\.?\d*)+\s*(\*|/)\s*(\d+\.?\d*)+')

    for match in multdiv.finditer(equation):
        if match.group(2) == '*':
            equation = equation.replace(match.group(0), f'{float(match.group(1)) * float(match.group(3))}')
        else:
            equation = equation.replace(match.group(0), f'{float(match.group(1)) / float(match.group(3))}')

    addsub = re.compile(r'(\d+\.?\d*)+\s*(\+|\-)\s*(\d+\.?\d*)+')

    for match in addsub.finditer(equation):
        if match.group(2) == '+':
            equation = equation.replace(match.group(0), f'{float(match.group(1)) + float(match.group(3))}')
        else:
            equation = equation.replace(match.group(0), f'{float(match.group(1)) - float(match.group(3))}')

    mathchars = ['^', '*', '/', '+', '-']
    negativenumber = re.compile(r'-(\d+\.?\d*)')
    for letter in equation:
        if letter in mathchars:
            if negativenumber.match(equation) is None:
                try:
                    return calculate_equation(equation)
                except RecursionError:
                    raise AttributeError("Equation not entered correctly, cannot reduce")

    return float(equation)


def calculate_grade(equation, values):
    """
    calculates the grade from the equation and plugs in the values

    :param equation: equation to calculate the grade from using variables t = num testcases, p = num testcases passed,
                                                                          m = bytes of memory leak, l = hours late
    :type equation: str
    :param values: the values of the variables in order: [t, p, m, l]
    :type values: list
    :return: int
    """
    variablelist = ['t', 'p', 'm', 'l']

    for i in range(len(values)):
        equation = equation.replace(variablelist[i], str(values[i]))

    return calculate_equation(equation)


#  testing code
if __name__ == '__main__':
    print(calculate_grade("100*(p/t)-m-10*l", [2, 1, 2, 1]))



