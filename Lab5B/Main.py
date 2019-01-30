#Ian Hudson Lab5 88609568
from Heap import Heap
import time

def heapSort(unsortedList):

    #Create a Heap for the sorting process
    heap = Heap()

    #For Loop to enter all the elements of the list into the heap
    for elem in unsortedList:
        heap.insert(elem)

    newList = []

    #insert all the elements in the heap into a new list
    while heap.isEmpty() is not True:
        val = heap.remove()
        newList.append(val)

    #return the new list
    return newList

def main():

    # Generating the 100 element list from a the fiile "values.txt"
    list5 = []
    counter = 0
    f = open("values.txt", 'r')
    for line in f:
        l = line.split(",")
        for elem in l:
            counter = counter + 1
            list5.append(int(elem))

    # 10 Element list with time stamps
    time1 = time.time()
    list1 = [5,2,4,70,16,22,6,9,12,33]
    newlist1 = heapSort(list1)
    time2 = time.time()

    # 25 element list with time stamps
    time3 = time.time()
    list2 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
    newlist2 = heapSort(list2)
    time4 = time.time()

    # 50 element list with time stamps
    time5 = time.time()
    list3 = [5, 55, 8, 42, 1000, 112, 67, 2, 222, 445, 65, 78, 98, 45, 446, 123, 234, 345, 654, 132, 33, 213, 556, 75,
             765, 7777, 3452252, 353, 6666, 66, 68, -405, 69, 71, 78, 79, 89, 45, 112, 232, 456, 567, 789, 987, 876, 98765,
             8766, 7665, 234324, 2452352, 46422, 6544]
    newlist3 = heapSort(list3)
    time6 = time.time()

    # 75 element list with time stamps
    time7 = time.time()
    list4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28,
                29, 30, 31, 32, 33, 34, 35, 36, 37,
                38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63,
                64, 65, 66, 67, 68, 69, 70, 71,
                72, 73, 74, 75]
    newlist4 = heapSort(list4)
    time8 = time.time()

    # 100 element list with time stamps
    time9 = time.time()
    newlist5 = heapSort(list5)
    time10 = time.time()

    print("-----------------")
    for elem in newlist1:
        print(elem)

    print("Time for n = 10 :", (time2-time1))

    print("-----------------")
    for elem in newlist2:
        print(elem)

    print("Time for n = 25:", (time4-time3))

    print("-----------------")
    for elem in newlist3:
        print(elem)

    print("Time for n = 50:", (time6-time5))

    print("-----------------")
    for elem in newlist4:
        print(elem)

    print("Time for n = 75:", (time8 - time7))

    print("-----------------")
    for elem in newlist5:
        print(elem)

    print("Time for n = 100:", (time10 - time9))





if __name__ == '__main__':
    main()