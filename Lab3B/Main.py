#Ian Hudson 88609568
from AVLtree import AVLTree
from AVLtree import AVLNode
from RBTree import RedBlackTree


global count


def general_anagrams(tree, word, prefix = "", printable = True):
    wordslist = []
    def print_anagrams(word, prefix):
            if len(word) <= 1:
                    str = prefix + word
                    temp = tree.search(str)
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


def countAnagrams(words, tree):
    maxLen = 0
    wordWithMostAnagrams = ""
    for elem in words:
        anagramCount = general_anagrams(tree,elem,"", False)
        if len(anagramCount) > maxLen:
            maxLen = len(anagramCount)
            wordWithMostAnagrams = elem
    print("The word with the most anagrams was", wordWithMostAnagrams, "with ", maxLen)





def main():

    treeType = input("To use an AVL Tree please Press a, to use a Red Black Tree please press b:")

    if treeType == "a" or treeType == "A":
        avlTree = AVLTree()
        print("Populating AVL Tree: ")
        f = open("Words", 'r')
        for line in f:
            l = line.split("\n")
            node = AVLNode(l[0])
            avlTree.insert(node)
        print("Tree Populated.")
        general_anagrams(avlTree, "money")

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

        countAnagrams(words2, avlTree)
        countAnagrams(words3, avlTree)
        countAnagrams(words4, avlTree)

    elif treeType == "b" or treeType == "B":
        rbTree = RedBlackTree()
        print("Populating Red Black Tree: ")
        f = open("Words", "r")
        for line in f:
            l = line.split("\n")
            rbTree.insert(l[0])
        print("Tree Populated.")
        general_anagrams(rbTree, "dog")

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

        countAnagrams(words2, rbTree)
        countAnagrams(words3, rbTree)
        countAnagrams(words4, rbTree)







if __name__ == '__main__':
    main()