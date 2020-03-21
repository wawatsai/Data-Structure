#factorial
def fact_fact(fact):
    correct = 1
    for i in range(1, fact+1):
        correct *= i
    return correct
print(fact_fact(5))
def fact_fact_2(fact):
    if fact == 1:
        return 1
    else:
        return fact * fact_fact_2(fact-1)
print(fact_fact_2(3))
def fact_fact_3(fact):
    if fact == 1:
        return 1
    else:
        return fact +    fact_fact_3(fact-1)
print(fact_fact_3(5))