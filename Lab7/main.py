#Ian Hudson 88609568

def editdistance(str1, str2):
    str1len = len(str1)
    str2len = len(str2)

    comparisonArray = [[0 for x in range(str1len+1)] for x in range(str2len+1)]

    for i in range(len(comparisonArray)):
        for j in range(len(comparisonArray[i])):
            if i == 0:
                comparisonArray[i][j] = j
            elif j == 0:
                comparisonArray[i][j] = i
            elif str1[i - 1] == str2[j-1]:
                comparisonArray[i][j] = comparisonArray[i-1][j-1]
            else:
                comparisonArray[i][j] = min(comparisonArray[i][j-1], comparisonArray[i-1][j], comparisonArray[i-1][j-1])


    for i in range(len(comparisonArray)-1):
        print(str1[i][0], end=" ")
    print("\n")
    for i in range(len(comparisonArray)):
        for j in range(len(comparisonArray[i])):
            print(comparisonArray[i][j], end=" ")
        print('\n')



def main():
    str1Array = []
    str2Array = []

    f = open("str1", 'r')
    for line in f:
        l = line.split("\n")
        for elem in l:
            str1Array.append(elem)

    f2 = open("str2", 'r')
    for line in f2:
        l = line.split("\n")
        for elem in l:
            str2Array.append(elem)

    for elem in str1Array:
        for elem2 in str2Array:
            print(elem,elem2)
            editdistance(elem,elem2)





if __name__ == '__main__':
    main()