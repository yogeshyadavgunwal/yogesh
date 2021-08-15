def divisonn(a, b):
    c = (a / b) * 100
    if c >= 60:
        print("first division")
    elif c >= 50:
        print("second division")
    elif c >= 33:
        print("third division")
    else:
        print("you are fail")