#Ian Hudson 88609568
class Node(object):
    id = 0
    next = None

    def __init__(self, id):
        self.id = id
        self.next = None


class LinkedList():
    def __init__(self):
        self.head = None

    def append(self, newid):

        newNode = Node(newid)

        if self.head is None:
            node = Node(newid)
            self.head = node
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = newNode

    def length(self):
        current = self.head
        counter = 0
        if current != None and current.next == None:
            return 1
        while current != None:
            current = current.next
            counter += 1
        return counter

    def print(self):
        if self.head is None:
            return
        else:
            current = self.head
            while current != None:
                print(current.id)
                current = current.next


def solution1(list):
    current1 = list.head
    collisioncount = []
    while current1 != None:
        current2 = list.head
        while current2 != None:
            if int(current1.id) == int(current2.id):
                collisioncount.append(int(current1.id))
            current2 = current2.next
        current1 = current1.next
    return collisioncount


def solution2(list):
    current1 = list.head
    while current1 != None:
        current2 = list.head
        while current2.next != None:
            if(int(current2.id) > int(current2.next.id)):
                temp = current2.id
                current2.id = current2.next.id
                current2.next.id = temp
            current2 = current2.next
        current1 = current1.next

    listofCollisions = []

    current1 = list.head
    while current1.next != None:
        if(int(current1.id) == int(current1.next.id)):
            listofCollisions.append(int(current1.id))
        current1 = current1.next

    return listofCollisions


def solution3(list):
    mergeSort(list.head)
    current = list.head
    listofCollisions = []

    while current.next != None:
        if(int(current.id) == int(current.next.id)):
            listofCollisions.append(int(current.id))
        current = current.next
    return listofCollisions


def mergeSort(list):

    if list is None or list.next is None:
        return list
    else:
        middle = getMiddleNode(list)
        nextmiddle = middle.next
        middle.next = None

        left = mergeSort(middle)
        right = mergeSort(nextmiddle)

        sortedList = sortMerged(left, right)

        return sortedList


def sortMerged(left, right):

    if left is None:
        return left
    elif right is None:
        return right

    if (int(right.id) <= int(left.id)):
        result = right
        result.next = sortMerged(right.next, left)
    else:
        result = left
        result.next = sortMerged(right, left.next)
    return result


def getMiddleNode(list):

    if list is None or list.next is None:
        return list
    else:
        fastpointer = list.next
        slowpointer = list

        while fastpointer != None:
            fastpointer = fastpointer.next
            slowpointer = slowpointer.next

        return slowpointer





def solution4(list):
    seenList = [None] * (list.length()+1)
    collisionList = []
    current = list.head
    while current != None:
        if(seenList[int(current.id)] == True):
            collisionList.append(current.id)
        else:
            seenList[int(current.id)] = True

        current = current.next
    return collisionList


def main():
    listsmall = LinkedList()
    with open('Sample1.1') as f:
        for line in f:
            listsmall.append(int(line))

    with open('Sample1.2') as f:
        for line in f:
            listsmall.append(int(line))

    listmedium = LinkedList()

    with open('Sample2.1') as f:
        for line in f:
            listmedium.append(int(line))

    with open('Sample2.2') as f:
        for line in f:
            listmedium.append(int(line))

    listLarge = LinkedList()

    with open('activision.txt') as f:
        for line in f:
            listLarge.append(int(line))

    with open('vivendi.txt') as f:
        for line in f:
            listLarge.append(int(line))

    print("Size of Merged List: " + str(listsmall.length()))
    print("solution 1: " + str(len(solution1(listsmall))))
    print("solution 2: " + str(len(solution2(listsmall))))
    print("solution 3: " + str(len(solution3(listsmall))))
    print("solution 4: " + str(len(solution4(listsmall))))

    print("Size of Merged List: " + str(listmedium.length()))
    print("solution 1: " + str(len(solution1(listmedium))))
    print("solution 2: " + str(len(solution2(listmedium))))
    print("solution 3: " + str(len(solution3(listmedium))))
    print("solution 4: " + str(len(solution4(listmedium))))

    print("Size of Merged List: " + str(listLarge.length()))
    print("solution 1: " + str(len(solution1(listLarge))))
    print("solution 2: " + str(len(solution2(listLarge))))
    print("solution 3: " + str(len(solution3(listLarge))))
    print("solution 4: " + str(len(solution4(listLarge))))



if __name__ == '__main__':
    main()
