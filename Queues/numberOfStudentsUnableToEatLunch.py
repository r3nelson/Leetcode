from typing import List


class ListNode:
    def __init__(self, val, next=None) -> None:
        self.val = val
        self.next = next


class Queue:
    def __init__(self) -> None:
        # queue will be list of ListNodes
        self.head = None
        self.tail = None
        self.length = 0

    # remove from beginning
    def dequeue(self):
        if not self.length:
            return

        poppedNode = self.head
        self.head = self.head.next

        self.length -= 1
        return poppedNode

    # append to end
    def enqueue(self, val):
        newNode = ListNode(val)

        if not self.tail:
            self.head = newNode
            self.tail = newNode

        self.tail.next = newNode
        self.tail = newNode

        self.length += 1
        return newNode

    def peek(self):
        if not self.head:
            return None
        return self.head.val

    def print(self):
        cur = self.head
        while cur:
            print(cur.val, " -> ", end="")
            cur = cur.next
        print()


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        # students will be queue
        studentQueue = Queue()
        # sandwiches will be stack
        sandwichesStack = []

        for i in range(len(students)):
            studentQueue.enqueue(students[i])
            sandwichesStack.append(sandwiches[len(sandwiches) - 1 - i])

        # check if student wants sandwich
        counter = 0
        while counter < studentQueue.length:
            if studentQueue.peek() == sandwichesStack[-1]:
                studentQueue.dequeue()
                sandwichesStack.pop()
                counter = 0
            else:
                node = studentQueue.dequeue()
                studentQueue.enqueue(node.val)
                counter += 1
        return counter
