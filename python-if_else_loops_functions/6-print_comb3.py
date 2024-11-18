#!/usr/bin/python3
for i in range(10):
    for j in range(i + 1, 10):
        # Print the combination using the format() method
        if i == 8 and j == 9:
            print("{}".format(i) + "{}".format(j))
        else:
            print("{}".format(i) + "{}".format(j), end=", ")
