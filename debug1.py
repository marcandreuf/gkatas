# Python's default arguments are evaluated 
# once when the function is defined, 
# not each time the function is called 
# (like it is in say, Ruby).

def f(i, values = []):
    values.append(i)
    print (id(values))
    print (values)
    return values
f(1)
f(2)
f(3)
