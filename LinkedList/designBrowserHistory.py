'''
Notes:

instead of setting cur to self.currentHistory I could just use self.currentHistory itself
'''

class ListNode:

    def __init__(self, url, leftNode = None, rightNode= None) -> None:
        self.url = url
        self.backHistory = leftNode
        self.forwardHistory = rightNode

# Doubly Linked List slower than stack for this problem
class BrowserHistory:

    def __init__(self, homepage: str):
        self.currentHistory = ListNode(homepage)
        
    def visit(self, url: str) -> None:
        cur = self.currentHistory
        newNode = ListNode(url, cur, None)
        cur.forwardHistory = newNode
        self.currentHistory = newNode
            

    def back(self, steps: int) -> str:
        cur = self.currentHistory

        while steps and cur.backHistory:
            cur = cur.backHistory
            steps -= 1

        self.currentHistory = cur

        return cur.url
        

    def forward(self, steps: int) -> str:
        cur = self.currentHistory

        while steps and cur.forwardHistory:
            cur = cur.forwardHistory
            steps -= 1

        self.currentHistory = cur

        return cur.url


# faster version using Stack
class StackImplementationBrowserHistory:

    def __init__(self,homepage:str) -> None:
        self.index = 0
        self.len = 1
        self.history = [homepage]

    def visit(self,url:str) -> None:
        # if history array isn't long enough just append value
        if len(self.history) < self.index+2:
            self.history.append(url)
        # if history array is long enough change value at self.index + 1
        else:
            self.history[self.index + 1] =url
        # change current index to new value and change length to self.index + 1 to soft delete the forwardHistory values
        self.index += 1
        self.len = self.index + 1

    def back(self,steps:int) -> str:
        self.index = max(self.index - steps, 0)
        return self.history[self.index]
    
    def forward(self,steps:int) -> str:
        self.index = min(self.index + steps, self.len -1)
        return self.history[self.index]
    
    

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)