#!/usr/bin/env python

"""
Problem:
    Given two linked lists in this format, return their sum in the same linked
    list format.

    Input: 1 -> 2 -> 3 -> 4 -> 5
    Output: 54321

    For example, given

    9 -> 9
    5 -> 2
    return 124 (99 + 25) as:

    4 -> 2 -> 1

References:
    Daily Coding Problem #452
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def number_from_list(head) -> int:
    result = []

    if head is None:
        return 0

    cur = head
    while True:
        result.append(cur.value)
        if cur.next is None:
            break
        cur = cur.next

    return int("".join([str(c) for c in result[::-1]]))

def split_number(number) -> list:
    
    return list(str(number))

def list_from_number(number: int) -> Node:

    number_list = split_number(number)
    reversed_list = number_list[::-1]

    head = Node(reversed_list[0])
    cur = head
    for n in reversed_list[1:]:
        cur.next = Node(n)
        cur = cur.next
    
    return head

def print_list(head):
    cur = head
    while True:
        print(cur.value+ " -> ", end=' ')
        if cur.next is None:
            print("None")
            break
        cur = cur.next

def sum_ll_number(list_head1: Node, list_head2: Node) -> int:
    """
    Time: O(N+M) N size(list1) M size(list2)
    Space: O(N+M)
    """
    number =  number_from_list(list_head1) + number_from_list(list_head2)

    return list_from_number(number)

if __name__ == '__main__':

    list_head1 = Node(1)
    list_head1.next = Node(2)
    list_head1.next.next = Node(3)
    list_head1.next.next.next = Node(4)
    list_head1.next.next.next.next = Node(5)

    #print(list_head1)
    #print(number_from_list(list_head1))

    for case in [(9,9,5,2), (1,5,2,1)]:
        l1 = Node(case[0])
        l1.next = Node(case[1])
        l2 = Node(case[2])
        l2.next = Node(case[3])
        print_list(sum_ll_number(l1, l2))


    # list_head1 = Node(9)
    # list_head1.next = Node(9)
    # list_head2 = Node(5)
    # list_head2.next = Node(2)
    # print_list(sum_ll_number(list_head1, list_head2))
    # print_list(sum_ll_number(list_head1, None))
