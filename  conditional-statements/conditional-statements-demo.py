if __name__ == '__main__':
    pass


def testIf(a, b):
    if a <= 3:
        pass
    elif b <= 5:
        print("okay")


## and
def logicalOperator(num):
    if 3 <= num <= 10:
        print("num is between 3 and 10, inclusive.")

    else:
        print("num is either less than 3 or greater than 10.")


## String Comparisons
def stringComparision():
    if "ryan" < "bob":
        print("AAA")
    elif "a" == "aaa":
        print("BBB")
    elif "gray" <= "grey":
        print("CCC")
    else:
        print("DDD")
