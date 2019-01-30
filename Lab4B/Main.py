#Ian Hudson 88609568
import time

global count

class HashTable():
    def __init__(self, size, type):
        self.table = [None] * size
        self.type = type


    def hash(self, k):
        if(self.type == 1):
            index = self.hash1(k)
        else:
            index = self.hash2(k)

        return index



    # This hash method simply multiplies the base 26 value by an irrelevant value for every
    # Letter in the word and then mods it by the table
    def hash1(self, k):
        hash = 7
        for elem in k:
            result = ord(elem)
            hash = hash + result
        return hash % len(self.table)

    # This Hash method creates an array of each ord value specified by its significance in the word,
    # then multiplies each value by 26 * the power of its significance and sums them, then returns the sum mod the
    # length of the table
    def hash2(self, k):
        hasha = []
        for elem in k:
            hasha.append(ord(elem))

        hash = 0
        for i in range(len(hasha)):
            temp = i+1 * 26 * hasha[i]
            hash += temp
        return hash % len(self.table)

    # This method inserts new elements into the table as either a new node at the hash index,
    # or adding the new node at the end of hte chain
    def insert(self, k):
        index = self.hash(k)
        if self.table[index] is None:
            self.table[index] = HashNode(k)
        else:
            current = self.table[index]
            while current.next is not None:
                current = current.next
            current.next = HashNode(k)

    # This method is used to search for elements by getting the Hash index and then following the Chain,
    # should the index have one
    def search(self, k):
        if k is None:
            return None
        index = self.hash(k)
        current = self.table[index]
        if current is None:
            print("None")
            return None
        else:
            while current.next is not None:
                if current.key == k:
                    return current
                current = current.next
            return None

    # This method is used to compute the Load Factor by counting the total number of elements,
    # then returning that count divided by the length of the table
    def loadfactor(self):
        counter = 0
        for i in range(len(self.table)):
            curr = self.table[i]
            while curr is not None:
                counter += 1
                curr = curr.next

        return counter / len(self.table)



class HashNode():

    def __init__(self, k):
        self.key = k
        self.next = None


# This method uses the same implementation as Lab3, except it uses the Table.search method
def general_anagrams(table, word, prefix = "", printable = True):
    wordslist = []
    def print_anagrams(word, prefix):
            if len(word) <= 1:
                    str = prefix + word
                    temp = table.search(str)
                    if temp is not None:
                        if printable:
                            print(temp.key)
                        wordslist.append(temp.key)
            else:
                for i in range(len(word)):
                    cur = word[i: i + 1]
                    before = word[0: i]
                    after = word[i + 1:]

                    if cur not in before:
                        print_anagrams(before + after, prefix + cur)
    print_anagrams(word, prefix)
    if printable:
        print("Anagram Count: ", len(wordslist))
    return wordslist

# This method uses the same implementation as in Lab3
def countAnagrams(words, table):
    maxLen = 0
    wordWithMostAnagrams = ""
    for elem in words:
        anagramCount = general_anagrams(table,elem,"", False)
        if len(anagramCount) > maxLen:
            maxLen = len(anagramCount)
            wordWithMostAnagrams = elem
    print("The word with the most anagrams was", wordWithMostAnagrams, "with ", maxLen)





def main():

    # Creating Three Tables:
    # Table1 with the size of the total number of words and hash function 1:

    table = HashTable(464455, 1)

    # Table2 with half the size of the total number of words and hash function 1:

    table2 = HashTable(232232, 1)

    # Table3 with twice of the size of the total number of words and hash function 1:

    table3 = HashTable(928910, 1)

    # Table4 with the size of the total number of words and hash function 2:

    table4 = HashTable(464455, 2)

    # Table5 with half the size of the total number of words and hash function 2:

    table5 = HashTable(232232, 2)

    # Table6 with twice of the size of the total number of words and hash function 2:

    table6 = HashTable(928910, 2)

    # Populates the Tables with the Words file:
    print("Populating Tables: ")
    f = open("Words", 'r')
    for line in f:
        l = line.split("\n")
        table.insert(l[0])
        table2.insert(l[0])
        table3.insert(l[0])
        table4.insert(l[0])
        table5.insert(l[0])
        table6.insert(l[0])
    print("Tree Populated.")

    # Tests to make sure the anagrams method works for the Hash Table Implementation
    general_anagrams(table, "money")

    # Checks the Three Word lists used in Lab3's Tests
    words2 = []
    f2 = open("wordstoSearch", "r")
    for line in f2:
        l = line.split("\n")
        words2.append(l[0])

    words3 = []
    f3 = open("morewords", "r")
    for line in f3:
        l = line.split("\n")
        words3.append(l[0])

    words4 = []
    f4 = open("mostestwords", "r")
    for line in f4:
        l = line.split("\n")
        words4.append(l[0])


    #The follow lines are test lines for the Anagram checks and Load Factors for
    #All Six Tables
    print("Results for Table with Hash Function 1, size: 464455")
    countAnagrams(words2, table)
    countAnagrams(words3, table)
    countAnagrams(words4, table)

    print("\nResults for Table with Hash Function 1, size: 232232")
    countAnagrams(words2, table2)
    countAnagrams(words3, table2)
    countAnagrams(words4, table2)

    print("\nResults for Table with Hash Function 1, size: 928910")
    countAnagrams(words2, table3)
    countAnagrams(words3, table3)
    countAnagrams(words4, table3)

    print("\nResults for Table with Hash Function 2, size: 464455")
    countAnagrams(words2, table4)
    countAnagrams(words3, table4)
    countAnagrams(words4, table4)

    print("\nResults for Table with Hash Function 2, size: 232232")
    countAnagrams(words2, table5)
    countAnagrams(words3, table5)
    countAnagrams(words4, table5)

    print("\nResults for Table with Hash Function 2, size: 928910")
    countAnagrams(words2, table6)
    countAnagrams(words3, table6)
    countAnagrams(words4, table6)

    print("\nLoad Factor for Table with Hash Function 1, Size: 464455: ", table.loadfactor())
    print("\nLoad Factor for Table with Hash Function 1, Size: 232232: ", table2.loadfactor())
    print("\nLoad Factor for Table with Hash Function 1, Size: 928910: ", table3.loadfactor())
    print("\nLoad Factor for Table with Hash Function 2, Size: 464455: ", table4.loadfactor())
    print("\nLoad Factor for Table with Hash Function 2, Size: 232232: ", table5.loadfactor())
    print("\nLoad Factor for Table with Hash Function 2, Size: 928910: ", table6.loadfactor())

    print(time.time())




if __name__ == '__main__':
    main()