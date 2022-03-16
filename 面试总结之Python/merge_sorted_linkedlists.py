"""
Merge K sorted linked lists
https://www.geeksforgeeks.org/merge-two-sorted-linked-lists/
https://www.geeksforgeeks.org/merge-k-sorted-linked-lists/
"""

import sys
from typing import List
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge3Lists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    p1, p2, p3 = lists[0], lists[1], lists[2]

    phead = ListNode()
    head = phead

    while (any(p is not None for p in [p1, p2, p3])):
        if (p1 is not None and
            (p2 is None or p1.val <= p2.val) and
            (p3 is None or p1.val <= p3.val)):
            temp = ListNode(p1.val)
            phead.next = temp
            phead = phead.next
            p1 = p1.next

        elif (p2 is not None and
            (p1 is None or p2.val <= p1.val) and
            (p3 is None or p2.val <= p3.val)):
            temp = ListNode(p2.val)
            phead.next = temp
            phead = phead.next
            p2 = p2.next

        elif (p3 is not None and
            (p1 is None or p3.val <= p1.val) and
            (p2 is None or p3.val <= p2.val)):
            temp = ListNode(p3.val)
            phead.next = temp
            phead = phead.next
            p3 = p3.next

    return head.next


# general solution for k lists
def merge3Lists1(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    head = ListNode()
    current = head

    while True:
        flag = False
        min = sys.maxsize
        index_of_min = 0

        for i in range(len(lists)):
            if (lists[i] is not None) and (lists[i].val < min):
                min = lists[i].val
                index_of_min = i
                flag = True

        if flag:
            lists[index_of_min] = lists[index_of_min].next

            temp = ListNode(min)
            current.next = temp
            current = current.next
        else:
            break

    return head.next


def print_lists(lists: List[Optional[ListNode]]) -> None:
    while lists is not None:
        print(f'{lists.val}', end=" ")
        lists = lists.next

    print()


if __name__ == '__main__':
    linked_list_1 = ListNode(1, ListNode(6, ListNode(8, ListNode(9, None))))
    linked_list_2 = ListNode(1, ListNode(3, ListNode(4, None)))
    linked_list_3 = ListNode(2, ListNode(7, None))

    merged_list = merge3Lists([linked_list_1, linked_list_2, linked_list_3])
    print_lists(merged_list)    # 1 1 2 3 4 6 7 8 9

    merged_list = merge3Lists1([linked_list_1, linked_list_2, linked_list_3])
    print_lists(merged_list)    # 1 1 2 3 4 6 7 8 9
