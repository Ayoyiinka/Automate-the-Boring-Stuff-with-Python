#Extending the Multiclipboard
'''Extend the multiclipboard program in this chapter so that it has a delete
<keyword> command line argument that will delete a keyword from the shelf.
Then add a delete command line argument that will delete all keywords.'''

import shelve, pyperclip, sys, os
os.chdir(r'C:\Users\EAGLE-AGE\Documents\Personal Projects\ATBSWP')

mcbShelf = shelve.open('mcb')

if len(sys.argv) == 3:
    if sys.argv[1].lower() == 'save':
        mcbShelf[sys.argv[2]] = pyperclip.paste
    elif sys.argv[1].lower() == 'delete':
        del mcbShelf[sys.argv[2]]
elif len(sys.argv) == 2:
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])
    elif sys.argv[1].lower() == 'delete':
        allkeys = list(mcbShelf.keys())
        for i in range(len(allkeys)):
            del mcbShelf[allkeys[i]]
mcbShelf.close()

#Mad Libs
'''Create a Mad Libs program that reads in text files and lets the user add
their own text anywhere the word ADJECTIVE, NOUN, ADVERB, or VERB
appears in the text file. For example, a text file may look like this:
The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was
unaffected by these events.
The program would find these occurrences and prompt the user to
replace them.
Enter an adjective:
silly
Enter a noun:
chandelier
Enter a verb:
screamed
Enter a noun:
pickup truck
The following text file would then be created:
The silly panda walked to the chandelier and then screamed. A nearby pickup
truck was unaffected by these events.
The results should be printed to the screen and saved to a new text file.'''

def madLibs(textFile):
    textF = open(textFile, 'r')
    textF = textF.read()
    for i in range(len(textF)):
        if textF[i:i+9].upper() == 'ADJECTIVE':
            print('Enter an adjective:')
            adj = input()
            textF = textF.replace('ADJECTIVE', adj, 1)
                    
        if textF[i:i+4].upper() == 'NOUN':
            print('Enter a noun:')
            noun = input()
            textF = textF.replace('NOUN', noun, 1)
                       
        if textF[i:i+4].upper() == 'VERB':
            print('Enter a verb:')
            verb = input()
            textF = textF.replace('VERB', verb, 1)
                      
        if textF[i:i+6].upper() == 'ADVERB':
            print('Enter an adverb:')
            adv = input()
            textF = textF.replace('ADVERB', adv, 1)

    print(textF)
    with open('newTextFile', 'w') as f:
        f.write(textF)

#Regex Search
'''Write a program that opens all .txt files in a folder and searches for any
line that matches a user-supplied regular expression. The results should
be printed to the screen.'''

import os, re

userDef = input()
userDefRegex = re.compile(userDef)
files = os.listdir(os.getcwd())
for i in range(len(files)):
    if files[i].endswith('.txt'):
        openFile = open(files[i], 'r')
        readFile = openFile.readlines()
        for j in range(len(readFile)):
            mo = userDefRegex.search(readFile[j])
            if mo != None:
                print(mo.group())

