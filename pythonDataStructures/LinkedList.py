class Node:
    def __init__(self, data=0):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, head=None):
        self.head = head
        self.length = 1 if head else 0

    def insert(self, data):
        # increment the lenght
        self.length += 1

        # take that data and insert at the end
        newNode = Node(data)

        if not self.head:
            self.head = newNode
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = newNode

    def display(self):

        temp = self.head

        while temp:
            print(temp.data, end=' -> ')
            temp = temp.next
        print('None')

    # insert anywhere

    def insertAt(self, data, index):
        if index < 0 or index > self.length:
            raise Exception("Index out of bounds!")

        self.length += 1

        newNode = Node(data)

        # if 0 then it becomes new head.
        if index == 0:
            newNode.next = self.head
            self.head = newNode
            return

        # if its at the end
        # get to tail node and
        # insert new node as next
        elif index == self.length:
            temp = self.head

            while temp.next:
                temp = temp.next

            temp.next = newNode

            return

        # last case is any where in between start and end

        # 5 -> 3

        # insert at index 1

        # 5 -> 22 -> 3

        # get both nodes

        # in this case since we want to insert at index 1
        # we want node 0 since having 5 will give us access
        # to 3 as well since its the next node.

        # do a for loop to get the node.

        # Then insert without orphaning the list

        # Point new node to next node
        # point next of the previous node
        # to new node
        temp = self.head
        for i in range(0, index - 1):
            temp = temp.next

        newNode.next = temp.next
        temp.next = newNode
        return

    def deleteAt(self, index):
        print("The index", index)
        if index < 0 or index > self.length - 1:
            raise Exception("Index out of bounds!")

        # if its at index 0, update head to head.next

        if index == 0:
            self.length -= 1
            self.head = self.head.next
            return

        # if its the last node then we will set previous
        # nodes next to null
        elif index == self.length - 1:
            self.length -= 1
            temp = self.head

            while temp.next.next:
                temp = temp.next

            temp.next = None
            return

        # last case where its actually between two nodes

        #  2 -> 3 -> 4

        # so now we want to remove 3.
        # we need access to 2 and 4.

        # we can point 2 to 3's next node and point 3 to null

        # so we need to get the one before the node we want to remove.

        # in this case we want to remove node 1, so we will get node 0
        # with the same loop as before.
        temp = self.head
        for i in range(0, index - 1):
            temp = temp.next

        # now we have the previous node to the one we want to remove

        # so get the one we need to remove as temp
        # get the one after that and connect previous to it
        # set the removed ones next to null
        print(temp.data)
        removedNode = temp.next
        temp.next = temp.next.next
        removedNode.next = None
        self.length -= 1

        return

    def reverseList(self):
        if not self.head or self.length == 1:
            return

        prev = None
        curr = self.head

        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        self.head = prev

    def reverseListRecursive(self):

        def recursiveReverse(head, prev):
            if head.next:
                recursiveReverse(head.next, head)
            else:
                self.head = head

            head.next = prev

        temp = self.head
        recursiveReverse(temp, None)


list = LinkedList()

list.display()

list.insert(5)
list.display()


list.insert(4)
list.display()

list.insert(3)
list.display()

list.insert(2)
list.display()

list.insert(1)
list.display()

list.insert(0)
list.display()

print("First reverse")
list.reverseList()
list.display()

print("Second reverse. Should undo previous reverse")
list.reverseListRecursive()
list.display()
