#!/usr/bin/env python

import sys

try:
    from pdb import break_on_setattr
    from mock import Mock
except ImportError:
    sys.stderr.write("Need to run: pip install mock pdbpp")
    sys.exit(1)

# @break_on_setattr("_arr")
class Node(object):
    def __init__(self, data):
        self._data = data
        self._left = None
        self._right = None
        self._arr = []

    def insert(self, value):
        if value <= self._data:
            if self._left is None:
                self._left = Node(value)
            else:
                self._left.insert(value)
        else:
            if self._right is None:
                self._right = Node(value)
            else:
                self._right.insert(value)

    def contains(self, value):
        if value == self._data:
            return True
        elif value < self._data:
            if self._left is None:
                return False
            else:
                return self._left.contains(value)
        else:
            if self._right is None:
                return False
            else:
                return self._right.contains(value)

    def in_order_arr(self, arr):
        if self._left is not None:
            self._left.in_order_arr(arr)
        arr.append(self._data)
        if self._right is not None:
            self._right.in_order_arr(arr)

        return arr

    def in_order(self):
        if self._left is not None:
            self._left.in_order()
        print("{0} ".format(self._data))
        if self._right is not None:
            self._right.in_order()

    def pre_order(self):
        print("{0} ".format(self._data))
        if self._left is not None:
            self._left.pre_order()
        if self._right is not None:
            self._right.pre_order()

    def post_order(self):
        if self._left is not None:
            self._left.post_order()
        if self._right is not None:
            self._right.post_order()
        print("{0} ".format(self._data))


def isBST(root):
    array = root.in_order_arr([])
    # print(array)
    size = len(array)
    for i in range(size-1):
        if array[i+1] <= array[i]:
            return False

    return True


def in_order_iter(root):
    result = []
    stack = []
    while len(stack) != 0 or root is not None:
        if root is not None:
            stack.append(root)
            root = root._left
        else:
            root = stack.pop()
            result.append(root._data)
            root = root._right

    return result


if __name__ == '__main__':

    root = Node(5)
    root.insert(3)
    root.insert(2)
    root.insert(7)

    print("""
          5
       3    7
    2
""")
    print("Contains 1", root.contains(1))
    print("Contains 3", root.contains(3))
    print("In order:")
    root.in_order()
    arr = []
    print(root.in_order_arr(arr))
    print("Pre order:")
    root.pre_order()
    print("Post order:")
    root.post_order()

    # import pdb; pdb.set_trace()
    print("Is Binary Search Tree ? ", isBST(root))

    print(in_order_iter(root))

    root = Node(1)
    root.insert(2)
    root.insert(2)
    root.insert(4)
    root.insert(5)
    root.insert(6)
    root.insert(7)

    print("Is Binary Search Tree ? ", isBST(root))
    print(in_order_iter(root))

    root = Mock()
    root.mock_add_spec(Node(7))
    expected = [1, 2, 3, 5]
    root.in_order_arr.return_value = expected
    print("Is Binary Search Tree ? ", isBST(root))
    print(expected)

    root = Mock()
    root.mock_add_spec(Node(7))
    expected = [2, 1, 3, 5]
    root.in_order_arr.return_value = expected
    print("Is Binary Search Tree ? ", isBST(root))
    print(expected)
