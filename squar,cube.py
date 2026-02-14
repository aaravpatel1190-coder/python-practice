def square (n):   #Defines a function named square, n is the number passed to the function
    return n*n    # multiplies n by itself
def cube  (n):
    return n*n*n

num=int(input("Enter a number:"))
print("square:",square(num))
print("cube:",cube(num))