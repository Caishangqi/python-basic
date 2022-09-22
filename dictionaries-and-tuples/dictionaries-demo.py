if __name__ == '__main__':

    # The whole collection page on lecture 8 page 58

    def basicDictionary():
        d = {'Aaron': 22, 'Richard': 40, 'Bobby': 18}
        print(d)
        print(d['Aaron'])


    # Dictionary Mutability
    def dictionaryMutability():
        garbage = {'abc': 88, 'xyz': 5.3, 'blah': 'hello', 2: 'nah'}
        garbage[1] = 'hi'
        garbage[3] = 58000
        garbage['yo'] = "yo"  # 添加到末尾
        print(garbage)  # {'abc': 88, 'xyz': 5.3, 'blah': 'hello', 2: 'nah', 1: 'hi', 3: 58000, 'yo': 'yo'}


    # The in Operator
    def inOperatorDictionary():
        staff_labels = {'Aaron': 'Lecturer', 'Matt': 'TA', 'Nikhil': 'TA'}
        print('Aaron' in staff_labels)


    # Traversing a Dictionary Keys
    def traverseDictionaryKeys():
        staff_labels = {'Aaron': 'Lecturer', 'Matt': 'TA', 'Nikhil': 'TA'}
        for name in staff_labels:
            print(name)  # name takes on each of the keys in the dictionary


    # Traversing a Dictionary Values
    def traverseDictionaryValues():
        staff_labels = {'Aaron': 'Lecturer', 'Matt': 'TA', 'Nikhil': 'TA'}
        for name in staff_labels:
            print(staff_labels[
                      name])  # To traverse the values of the dictionary, we would merely need to index into thedictionary with each key


    # Traversing a Dictionary Values
    def traverseDictionaryValues2():
        staff_labels = {'Aaron': 'Lecturer', 'Matt': 'TA', 'Nikhil': 'TA'}
        for label in staff_labels.values():
            print(label)


    # Using items method traverse
    def traverseDictionaryItems():
        staff_labels = {'Aaron': 'Lecturer', 'Matt': 'TA', 'Nikhil': 'TA'}
        for (key, label) in staff_labels.items():
            print("{} is a {}".format(key, label))


    traverseDictionaryItems()
