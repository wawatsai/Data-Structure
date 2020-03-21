print("Do NOt input \"0\" or \"less than 0\"!!")
import time
while True:
    input_number = int(input("Please input a number: "))
    start = time.time()
    def Fibonacci(your_index):
        if your_index <= 2 and your_index > 0:
            return 1
        elif your_index < 1:
            return "Oh No, you should input a number that is greater than 0!!"
        else:
            return Fibonacci(your_index-1)+Fibonacci(your_index-2)
    print("The result of fibonacci of the index", input_number,"is:",Fibonacci(input_number))
    print(time.time()-start)