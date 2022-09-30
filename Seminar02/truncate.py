import math

def truncate(real_num, num_of_decimals):
    magnitude = 10 ** num_of_decimals
    real_num = math.trunc(real_num * magnitude)
    return real_num / magnitude

print(truncate(10.789999, 2))
