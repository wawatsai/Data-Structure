while True:
    input_f = int(input("Please input a number that has no dots: "))
    def interactive(f):
        if f < 0: return "Please do not type a number that is less than 0!!"
        elif f == 0: return 0
        elif f < 2: return 1
        a = b = 1
        for i in range(2, f):
            a, b = b, a + b
        return b
    print(interactive(input_f))