#Author: Gloria Ngan
#LetterCounter.py

# This is a program that counts the lines in a file, then generates a
# random number no greater than the number of lines for each line. A
# word corresponding to each random number is retrieved and the occurences
# of each letter are counted and saved.

import random

#Writes out alphabet bc I am too lazy to hardcode it.
def writeAlpha(alphabet):
    #ASCII 97-122 is lowercase alphabet.
    i = 97
    while i < 122:
        alphabet.append(chr(i))
        i = i+1     
    return alphabet

#Counts and returns the number of words in a file.
def countLines(file1):
    i = 0
    for line in file1:
        if line != " ":
            i += 1
    return i

#Gets the lines corresponding to the randomized numbers.
def getLines(fid, randomNumbers, wordList, charsList):
    count = 0
    for randint in randomNumbers:
        line = fid.readline()
    
        while count <= randint:
            line = fid.readline()
            count += 1   
            
        word = line.strip()
        wordList.append(word)
        charsList += word
        
    charsList.sort()     #Sorts letters alphabetically.
    return count

#Counts the letters in charsList.
def countLetters(charsList, letterCount):
    i = 0
    occurrence = 0
    while i < len(charsList) - 1:
        if charsList[i] == charsList[i+1]:
            occurrence += 1
        else:
            letterCount.append(occurrence+1)
            occurrence = 0
        i = i+1
    letterCount.append(occurrence+1)

#Writes the words to a file.
def writeRandomWords(filename, lineCount, wordsList):
    i = 0
    fid = open(filename, 'w')       #Opens file for writing; 'w'.
    while i < 100:
        line = '%d\t\t%d\t\t%s\n' %(i, randomNumbers[i], wordsList[i])
        fid.write(line)
        i += 1
    fid.close()

#Writes the letter and the times it occurs in two columns.
def writeLetterCount(filename, alphabet, letterCount):
    i = 0
    fid = open(filename, 'w')
    while i < len(letterCount):
        line = '%s\t\t%d\n' %(alphabet[i], letterCount[i])
        fid.write(line)
        i += 1
    fid.close()

#Writes the histogram for the occurrences of each letter.
def writeHistogram(filename, alphabet, letterCount):
    i = 0
    fid = open(filename, 'w')
    while i < len(letterCount):
        line = '%s\n' %(alphabet[i]*letterCount[i])
        fid.write(line)
        i += 1
    fid.close()

#Method calls.
fid = open("E:\\CompSci\\Python\\words.txt","rb")

#Counts lines and prints number.
lineCount = countLines(fid)
print"Number of lines:"
print lineCount
print""

#Randomizes numbers for each line.
randomNumbers = [random.randint(1, lineCount) for i in range(100)]
randomNumbers.sort()
print"Random numbers:"
print randomNumbers
print""

fid = open("E:\\CompSci\\Python\\words.txt")
wordsList = []
charsList = []
letterCount = []
getLines(fid, randomNumbers, wordsList, charsList)

#Prints results.
print"List of words corresponding to Random Numbers:"
print wordsList
print""
print"Character list:"
print charsList
print""
countLetters(charsList, letterCount)
print"The number of occurrences of each letter:"
print letterCount
print""

alphabet = []
writeAlpha(alphabet)

#Writes to external file.
writeRandomWords('E:\\CompSci\\Python\\randomWords.txt', lineCount, wordsList)
writeLetterCount('E:\\CompSci\\Python\\letterCount.txt', alphabet, letterCount)
writeHistogram('E:\\CompSci\\Python\\histogram.txt', alphabet, letterCount)
