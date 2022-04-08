while True:
    response = input("Age: ")
    if response < 4:
        price = 0
    elif response < 18:
        price = 25
    elif response == 'q':
        break
    else:
        price = 40
