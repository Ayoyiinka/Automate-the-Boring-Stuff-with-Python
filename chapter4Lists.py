'''Write a function that takes a list value as an argument and returns a string with all the items separated by a comma and a space, 
with and inserted before the last item. But your function should be able to work with any list value passed to it.'''
#Commma Code
def listToText(listt):
    text = ''
    for i in range(len(listt) - 1):
        text += str(listt[i]) + ', '
    text = text + 'and ' + str(listt[-1])
    return text

spam = ['apples', 'bananas', 'tofu', 'cats', 'yam', 'egg', 1, 3]
spamText = listToText(spam)
print(spamText)

#Character Picture Grid
'''Say you have a list of lists where each value in the inner lists is a one-characterstring, like this(grid variable):

grid = [['.', '.', '.', '.', '.', '.'],
['.', 'O', 'O', '.', '.', '.'],
['O', 'O', 'O', 'O', '.', '.'],
['O', 'O', 'O', 'O', 'O', '.'],
['.', 'O', 'O', 'O', 'O', 'O'],
['O', 'O', 'O', 'O', 'O', '.'],
['O', 'O', 'O', 'O', '.', '.'],
['.', 'O', 'O', '.', '.', '.'],
['.', '.', '.', '.', '.', '.']]

'''You can think of grid[x][y] as being the character at the x- and y-coordinates of a “picture” drawn with text characters. The (0, 0) 
origin will be in the upper-left corner, the x-coordinates increase going right, and w the y-coordinates increase going down.Copy the 
previous grid value, and write code that uses it to print the image below:
..OO.OO..
.OOOOOOO.
.OOOOOOO.
..OOOOO..
...OOO...
....O....
'''

for i in range(len(grid[0])):
    for j in range(len(grid)):
        print(grid[j][i], end='')
    print()
