def normal_print(**kwargs):
    print(kwargs)

def print_nicely(**kwargs):
    normal_print(**kwargs)
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_nicely(name='Angga', age='27')