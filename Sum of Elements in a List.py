def sum_list(lst):
    total = 0
    for i in lst:
        total = total + i
    return total

numbers = [2, 4, 6, 8]
print("Sum =", sum_list(numbers))