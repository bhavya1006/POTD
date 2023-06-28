# User function Template for python3

def checkInLinkedList(data, head):
    while head:
        if head.data == data:
            return True
        head = head.next
    return False


class Solution:
    def union(self, head1, head2):
        ll = linkedList()
        s = set()

        for x in [head1, head2]:
            while x:
                s.add(x.data)
                x = x.next
        l = list(s)
        l.sort()
        for x in l:
            ll.insert(x)
        return ll.head


# {
 # Driver Code Starts
# Initial Template for Python 3

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class linkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, data):
        if self.head is None:
            self.head = Node(data)
            self.tail = self.head
        else:
            self.tail.next = Node(data)
            self.tail = self.tail.next


def printList(head):
    while head:
        print(head.data, end=' ')
        head = head.next


if __name__ == '__main__':
    for _ in range(int(input())):

        n1 = int(input())
        arr1 = [int(x) for x in input().split()]
        ll1 = linkedList()
        for i in arr1:
            ll1.insert(i)

        n2 = int(input())
        arr2 = [int(x) for x in input().split()]
        ll2 = linkedList()
        for i in arr2:
            ll2.insert(i)

        ob = Solution()
        printList(ob.union(ll1.head, ll2.head))
        print()

# } Driver Code Ends
