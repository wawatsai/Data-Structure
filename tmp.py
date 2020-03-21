picture = {1:2,
           10: 200}
while True:
    input_dict = int(input("Please input a number: "))
    get = picture.get(input_dict)
    if  get != None:
        print(get)
    else:
        print(None)