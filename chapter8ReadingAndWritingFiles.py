#!python3

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


