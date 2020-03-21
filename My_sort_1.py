import time
import random
random_list = [random.randrange(10000) for _ in range(10000)]
answer_list = random_list[:]
data = []
time_start = time.time()
def min_my(data):
    correct = float('inf')
    for data_correct in data:
        if data_correct < correct:
            correct = data_correct
    return correct
while random_list:
    data.append(min_my(random_list))
    random_list.remove(min_my(random_list))
print(data)
end = time.time()
print("\n\n\n\n")
print("The time is:", end - time_start)