if __name__ == '__main__':
    def hello_world():
        print("Hello, World!")


    # Arguments/Parameters
    def numberReturn(x):
        return x + 2


    # Global Variables
    a = 12


    def globalVariable():
        global a
        print(a)
        a = 70
        print(a)


    # Optional Arguments
    def optionalArguments(name, msg="hello"):
        print("{},{}".format(msg, name))


    hello_world()
    globalVariable()
    optionalArguments("Caizii")
    optionalArguments("Ruby", msg="Fuck you")
