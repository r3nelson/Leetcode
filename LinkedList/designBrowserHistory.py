'''
Notes:

instead of setting cur to self.currentHistory I could just use self.currentHistory itself
'''

class ListNode:

    def __init__(self, url, leftNode = None, rightNode= None) -> None:
        self.url = url
        self.backHistory = leftNode
        self.forwardHistory = rightNode

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

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)