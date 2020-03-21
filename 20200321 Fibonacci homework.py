memory = {0: 0, 1: 1, 2: 1}
def function(f):
    if f in memory: return memory[f]
    elif f < 0: return 0
    correct = function(f-1) + function(f-2)
    memory[f] = correct
    return correct
print(function(-12))