def decorator_with_argument(arg_1, arg_2):
    print(arg_1, arg_2)
    def inner1(func):
        def inner2(a, b):
            
            print("before Execution")
            
            # getting the returned value
            returned_value = func(a, b)
            print("after Execution")
            
            # returning the value to the original frame
            return returned_value
            
        return inner2
    return inner1
 
 
# adding decorator to the function
@decorator_with_argument("Ini team 5", "ini hari sabtu")
def sum_two_numbers(a, b):
    print("Inside the function")
    return a + b
 
@decorator_with_argument("Ini team 5", "ini hari sabtu")
def subtract_two_numbers(a, b):
    return a - b

a, b = 1, 2
 
# getting the value through return of the function
print("Sum =", sum_two_numbers(a, b))