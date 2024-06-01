def multiply(*args):
    print(args)
    total = 1
    for arg in args:
        total *= arg
    return total

def apply(operator, *args):
    if operator == "+":
        return sum(args)
    elif operator == "*":
        return multiply(args)
    else:
        return "BUGS!"
    
# print(apply(1,2,3,4, "*"))
print(apply("*", 1,2,3,4))