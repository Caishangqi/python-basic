if __name__ == '__main__':
    def listBasic():
        my_first_list = ["Aaron", "Ryan", "Monica", "Bobby", "Hillary"]
        print(my_first_list)


    def listBasic1():
        fruits = ["apple", "banana", "orange", "avocado"]
        print(fruits[0])


    # Lists are Mutable
    def listMutable():
        stuff2 = ['def', 'hello', 8, '2 + 2']
        stuff2[2] = "AAA"
        print(stuff2)


    # The in Operator
    def listInOperator():
        staff = ["aaron", "matt", "nikhil", "sanjat", "jiarui"]
        print("matt" in staff)  # 判断


    # The del Operator
    def listDelOperator():
        staff = ["aaron", "matt", "nikhil", "sanjat", "jiarui"]
        del staff[0]
        print(staff)


    # String Method: split()
    def listSplit():
        chars = "abcde"
        list[str] = chars.split('b')
        print(list)


    # String Method: append()
    def listAppend():  # 单个添加
        coins = ["penny", "nickel", "dime"]
        coins.append("quarter")
        print(coins)


    # String Method: extend()
    def listExtend():  # 多个添加
        coins = ["penny", "nickel", "dime"]
        coins.extend(["half dollar", "dollar"])
        print(coins)


    listExtend()
