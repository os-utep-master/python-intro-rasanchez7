'''
Created on Sep 1, 2019

@author: Ricardo Sanchez
'''
import sys        # command line arguments
import os         # checking if file exists
 
#Checking initial conditions (Samples taken from wordCountTest) 
if len(sys.argv) is not 3:
    print("Correct usage: wordCount.py <input text file> <output file> ")
    exit()

inputFname = sys.argv[1]
outputFname = sys.argv[2]

#make sure input file exist
if not os.path.exists(inputFname):
    print ("text file input %s doesn't exist! Exiting" % inputFname)
    exit()
    
#make sure output file exists
if not os.path.exists(outputFname):
    print ("wordCount output file %s doesn't exist! Exiting" % outputFname)
    exit()


#open file and create initial list of words
open_file = open(inputFname, "r")
stri= ""

for line in open_file:
    stri+=line 
word_stri = stri.split()
open_file.close()


#punctuation and sorting of words
count = 0
while count < len(word_stri):
    if "," in word_stri[count] or "." in word_stri[count] or ":" in word_stri[count] or ";" in word_stri[count]:
        word_stri[count] = word_stri[count].translate({ord(i): None for i in ',.:;'})
    if "--" in word_stri[count]:
        word_stri[count] = word_stri[count].replace('--', '-')
    if "-" in word_stri[count]:
        word_stri.append(word_stri[count].split('-')[1])
        word_stri[count] = word_stri[count].split('-')[0]
    word_stri[count] = word_stri[count].lower()
    count += 1
word_stri.sort()

#count of words
newList =[]
index = 0
curCount = 0
tempString =""
while index < len(word_stri):
    curCount = word_stri.count(word_stri[index])
    tempString = word_stri[index] + " " + str(curCount)
    newList.append(tempString) 
    index += curCount
    
#writing output file
with open(outputFname, 'w') as f:
    for item in newList:
        f.write("%s\n" % item)
