
# We want to initialize a 2d list 10 rows x 12 columns with ZEROs

# ex 1. simple list of 12 ZEROs
simple_list = [0] * 12
# print(simple_list)

double_list = [[0] * 12 for i in range(10)] 
double_list[3][4] = 22
print(double_list)