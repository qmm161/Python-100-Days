def multi_table(start = 1, end = 9) :
    for row in range(start, end + 1) :
        for i in range(1, row + 1) :
            print("{0}*{1}={2}".format(i, row, i * row), end=' ')
        print("")

if __name__ == "__main__" :
    multi_table(1,9)