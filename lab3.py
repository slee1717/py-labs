def max_num_func(x):
    if len(x) == 1:
        return x[0]

    y = len(x) // 2
    left_half = x[:y]
    right_half = x[y:]

    max_left = max_num_func(left_half)
    max_right = max_num_func(right_half)

    if max_left > max_right:
        return max_left
    else:
        return max_right

#Test Cases:
example = [5,6,4,7,3,9]
result = max_num_func(example)
print("Max Value:", result)