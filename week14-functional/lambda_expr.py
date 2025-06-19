def my_function(x):
    return x * x * x 



a = my_function(3)
print(a)

use_lambda = lambda v : print(my_function(v))

use_lambda(3)