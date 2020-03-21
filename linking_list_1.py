class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
class Linking_List:
    def __init__(self):
        self.head = Node(0)
    #add_append is add something in the Linking_list
    def add_append(self, value):
        node = Node(value)
        run = self.head
        while run.next is not None:
            run = run.next
        else:
            run.next = node
    #This print_All is print all
    def print_All(self):
        run_1 = self.head.next
        while run_1 is not None:
            print(run_1.value)
            run_1 = run_1.next
        else:
            print("done")
    def get(self, index:int):
        count = 0
        run_1 = self.head.next
        while run_1 is not None:
            if count == index:
                return run_1.value
            run_1 = run_1.next
            count += 1
    def __len__(self):
        run_1 = self.head.next
        count = 0
        while run_1 is not None:
            run_1 = run_1.next
            count += 1
        else:
            return count
    def remove(self, index):
        run_1 = self.head
        count = 0
        while run_1.next is not None:
            if count == index:
                run_1.next = run_1.next.next
                break
            run_1 = run_1.next
            count += 1
            
my_list = Linking_List()
my_list.add_append("hellooo")
my_list.add_append("I")
my_list.add_append("am")
my_list.add_append("Allen")
my_list.add_append(".")
my_list.add_append("Nice")
my_list.add_append("to")
my_list.add_append("meet")
my_list.add_append("you")
my_list.add_append("!")
#print(len(my_list))
my_list.remove(2)
my_list.print_All()
#print(my_list.head.next.next.value)
#my_list.print_All()
#print(my_list.get(1))
#print(my_list.length())