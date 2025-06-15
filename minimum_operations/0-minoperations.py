#!/usr/bin/python3
"""In a text file, there is a single character H. Your text editor can execute
only two operations in this file: Copy All and Paste. Given a number n, write
a method that calculates the fewest number of operations needed to result in
exactly n H characters in the file.
"""


def minOperations(n):
    if n < 2:
        return 0

    h_num = 1
    copy_num = 0
    op_num = 0
    while h_num < n:
        if n % h_num == 0:
            copy_num = h_num
            op_num += 1

        h_num += copy_num
        op_num += 1
    return op_num
