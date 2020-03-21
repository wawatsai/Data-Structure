memory = {0: 0, 1: 1, 2: 1}
while True:
    input_memory = int(input("Please input a number that has no dots: "))
    def function(f):
        if f in memory: return memory[f]
        elif f < 0: return "You can\'t type less than 0!!"
        correct = function(f-1) + function(f-2)
        memory[f] = correct
        return correct
    print(function(input_memory))