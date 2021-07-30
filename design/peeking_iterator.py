"""
Design an iterator that supports the peek operation on a list in addition to the hasNext and the next operations.

Implement the PeekingIterator class:

PeekingIterator(int[] nums) Initializes the object with the given integer array nums.
int next() Returns the next element in the array and moves the pointer to the next element.
bool hasNext() Returns true if there are still elements in the array.
int peek() Returns the next element in the array without moving the pointer.
"""


class PeekingIterator(object):
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iter = iterator
        self.next_val = iterator.cul() if iterator.hasNext() else None

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self.next_val

    def next(self):
        """
        :rtype: int
        """
        temp = self.next_val
        self.next_val = self.iter.cul() if self.iter.hasNext() else None
        return temp

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.next_val is not None


if __name__ == "__main__":
    li = "heelo"
    s = PeekingIterator()
    if s.hasNext():
        s.next()
    print(s.peek())
    print(s.next())
    print(s.next())