if __name__ == '__main__':
    # str
    def stringBasic() -> object:
        return type(str(3))


    # len()
    def stringBasic1():
        return len("abcd")


    # Traversing a String
    def traverseString():
        chars = "abcde"
        for c in chars:
            print(c)


    traverseString()
