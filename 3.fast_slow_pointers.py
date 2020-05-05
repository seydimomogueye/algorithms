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


def has_cycle(head):
    """
    Given the head of a Singly LinkedList, write a function to determine if the LinkedList has a cycle in it or not.
    """
    pass


def find_cycle_start(head):
    """
    Given the head of a Singly LinkedList that contains a cycle, write a function to find the starting node of the cycle.
    """
    pass


def find_happy_numbers(N):
    """
    Any number will be called a happy number if, after repeatedly replacing it with a number equal to the sum of the square of all of its digits, 
    leads us to number ‘1’.
    All other (not-happy) numbers will never reach ‘1’. 
    Instead, they will be stuck in a cycle of numbers which does not include ‘1’.
    """
    pass


def middle_of_linked_list(head):
    """
    Given the head of a Singly LinkedList, write a method to return the middle node of the LinkedList.

    If the total number of nodes in the LinkedList is even, return the second middle node.
    """
    pass


def is_palindromic_linked_list(head):
    """
    Given the head of a Singly LinkedList, write a method to check if the LinkedList is a palindrome or not.

    Your algorithm should use constant space and the input LinkedList should be in the original form once the algorithm is finished. The algorithm should have O(N)O(N) time complexity where ‘N’ is the number of nodes in the LinkedList.
    """
    pass


def reorder(head):
    """
    Rearrange a LinkedList (medium) #
    Given the head of a Singly LinkedList, write a method to modify the LinkedList such that the nodes from the second half of the LinkedList are inserted alternately to the nodes from the first half in reverse order. So if the LinkedList has nodes 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> null, your method should return 1 -> 6 -> 2 -> 5 -> 3 -> 4 -> null.
    """
    pass


def circular_array_loop_exists(A):
    """
    We are given an array containing positive and negative numbers. 
    Suppose the array contains a number ‘M’ at a particular index. 
    Now, if ‘M’ is positive we will move forward ‘M’ indices and if ‘M’ is negative move backwards ‘M’ indices. 
    You should assume that the array is circular which means two things:
        1. If, while moving forward, we reach the end of the array, we will jump to the first element to continue the movement.
        2. If, while moving backward, we reach the beginning of the array, we will jump to the last element to continue the movement.
    Write a method to determine if the array has a cycle. The cycle should have more than one element and should follow one direction which means the cycle should not contain both forward and backward movements.
    """
    pass
