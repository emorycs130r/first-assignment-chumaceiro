def expression_1(x):

    return (x ** 3) - ((2 * x)+(x ** 2)) - 100
        

def expression_2(x, y):

    return ((x ** 4)/(2 * y)) - (3 * x * y) + ((6 * y)/(7 * x))
    


def expression_3(x, y):
    
    return ((x ** 3) + (y ** 2)) / ((x ** 2) + (y ** 3))

if __name__ == "__main__":
    
    print(expression_1(4))
    print(expression_2(2, 4))
    print(expression_3(1, 1))