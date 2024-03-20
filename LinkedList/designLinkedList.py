'''
Notes:

Dummy Nodes:
When doing linked list problems you can use dummy nodes so you don't have to worry about edge cases.
The dummy nodes don't matter because we always start iterating with the node after our left dummy node and we only append before our right dummy node

Initalizing ListNode:
When initalizing ListNode you can add leftNode and rightNode param and default them to None. This will allow you to plug in directly if you already have the Nodes though

Use Range:
Another way of finding the value at the index is to use the range function instead of decrementing the index

Add a length property to LinkedList:
This will make it easy to check length later on

General:
When using classes in python put a '_' in front of private methods (methods that should only be used in the backend)
when using for loop if you can use '_' as a placeholder value so you don't get that squiggly line error for not using the loop iterator value
python by default returns None, so even if you don't have a return statement in your function the return type is None
e.g. (both return None)
def my_function():  
    pass
or
def my_function():
    return
'''

class ListNode:
    def __init__(self, val) -> ListNode:
        self.val = val
        self.prev = None
        self.next = None

class MyLinkedList:

    def __init__(self):
        # create two dummy nodes as head and tail
        self.left = ListNode(float('-inf'))
        self.right = ListNode(float('inf'))
        self.left.next = self.right
        self.right.prev = self.left
        
    def get(self, index: int) -> int:
        # start at node after left
        cur = self.left.next
        while cur and index > 0 :
            cur = cur.next
            index -= 1
            
        
        if cur and cur != self.right and index == 0:
            return cur.val

        return -1
        
    def addAtHead(self, val: int) -> None:
        # change left node to point to new head and vice versa
        node, prev, next = ListNode(val), self.left, self.left.next

        prev.next = node
        next.prev = node
        node.next = next
        node.prev = prev

    def addAtTail(self, val: int) -> None:

        # change right node to point to new tail and vice versa
        node, prev, next = ListNode(val), self.right.prev, self.right

        prev.next = node
        next.prev = node
        node.next = next
        node.prev = prev

    def addAtIndex(self, index: int, val: int) -> None:
        # start at node after left
        cur = self.left.next

        while cur and index > 0 :
            cur = cur.next
            index -= 1

        if cur and index == 0:
                node, prev, next = ListNode(val), cur.prev, cur
                prev.next = node
                next.prev = node
                node.next = next
                node.prev = prev
              

    def deleteAtIndex(self, index: int) -> None:
        # start at node after left
        cur = self.left.next
       
        while cur and index > 0:
            cur = cur.next
            index -= 1

        if cur and cur != self.right and index == 0:
            prev, next =  cur.prev, cur.next
            prev.next = next
            next.prev = prev
            
        
# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)