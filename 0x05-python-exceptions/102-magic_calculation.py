def magic_calculation(a, b): 
    result = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception("Too Far")
            else:
                result += a * b // i
        except ArithmeticError:
            result = a + b
            break

    return result
