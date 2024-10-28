# ID Number: 620170333
# Hackerrank Handle: antoniokerruni
# Hackerrank Exercise: Standard Deviation 1

#Code submission from Hackerrank:

def standDev(a, b, c, d, e, f, g, h, i, j):
    
    #code finds mean 
    mean = ( a + b + c + d + e + f + g + h + i + j ) / 10

    #code subtracts mean from each original data point
    result_a = a - mean
    result_b = b - mean
    result_c = c - mean
    result_d = d - mean
    result_e = e - mean
    result_f = f - mean
    result_g = g - mean
    result_h = h - mean
    result_i = i - mean
    result_j = j - mean

    #code squares each result
    sqr_result_a = result_a ** 2
    sqr_result_b = result_b ** 2
    sqr_result_c = result_c ** 2
    sqr_result_d = result_d ** 2
    sqr_result_e = result_e ** 2
    sqr_result_f = result_f ** 2
    sqr_result_g = result_g ** 2
    sqr_result_h = result_h ** 2
    sqr_result_i = result_i ** 2
    sqr_result_j = result_j ** 2

    #code adds up all squares
    sqr_total = (sqr_result_a + sqr_result_b + sqr_result_c + sqr_result_d +
                 sqr_result_e + sqr_result_f + sqr_result_g + sqr_result_h +
                 sqr_result_i + sqr_result_j)

    #code divides by number of data points
    sqr_variance = sqr_total / 10

    #code gets square root of value obtained
    std_div = round(math.sqrt(sqr_variance), 3)

    #code prints value obtained
    return (std_div)
    
