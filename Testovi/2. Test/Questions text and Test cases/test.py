if __name__ == '__main__':

    test = [1, 2]
    test[0], test[1] = test[1], test[0]
    print(test)