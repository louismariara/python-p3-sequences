#!/usr/bin/env python3

def print_fibonacci(length):
    my_fibonacci=[0,1]
    if length == 0:
        print("[]")
    elif length == 1:
        print("[0]")
    else:
        for i in range(2, length):
            my_fibonacci.append(my_fibonacci[i-1]+my_fibonacci[i-2])
        print(my_fibonacci)
print_fibonacci(10)