def addition(a,b):
    sum = a+b
    result = { 'value': sum}
    return result


def sub(a,b):
    diff = a-b
    result = { 'value': diff}
    return result


def multiply(a,b):
    m = a*b
    result = { 'value': m}
    return result


def divide(a,b):
    if b == 0:
        x = "Please enter a non zero divisor"
        result = {'value': x}
    else:
        d = a/b
        result = { 'value': d }
    return result
