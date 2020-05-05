class Node:

    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def print_list(self):
        temp = self
        while temp is not None:
            print(temp.value, end=" ")
            temp = temp.next
        print()


def reverse_linked_list(head):
    """
    Given the head of a Singly LinkedList, reverse the LinkedList.
    Write a function to return the new head of the reversed LinkedList.
    """
    pass


def reverse_sub_list(head, p, q):
    """
    Given the head of a LinkedList and two positions ‘p’ and ‘q’, reverse the LinkedList from position ‘p’ to ‘q’.
    """
    pass

def reverse_every_k_elements(head, k):
    """
    Given the head of a LinkedList and a number ‘k’, reverse every ‘k’ sized sub-list starting from the head.

    If, in the end, you are left with a sub-list with less than ‘k’ elements, reverse it too.
    """
    pass


def reverse_alternate_k_elements(head, k):
    """
    Given the head of a LinkedList and a number ‘k’, reverse every alternating ‘k’ sized sub-list starting from the head.

    If, in the end, you are left with a sub-list with less than ‘k’ elements, reverse it too.
    """
    pass


def rotate(head, rotations):
    """
    Given the head of a Singly LinkedList and a number ‘k’, rotate the LinkedList to the right by ‘k’ nodes.
    """
    pass