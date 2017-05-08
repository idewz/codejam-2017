from sys import argv



if __name__ == '__main__':
    test_cases = open(argv[1])
    t = int(test_cases.readline())

    for i in range(0, t):
        input = test_cases.readline()
        print(input)

    test_cases.close()
