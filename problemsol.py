while True:
    try:
        nums = int(input("Enter a number: "))

        if nums % 2 == 0:
            print("Even")
        else:
            print("Odd")

        break   # stops the loop if everything works

    except:
        print("Please enter a valid number.")
