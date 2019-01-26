# Strong Password Detection
'''Write a function that uses regular expressions to make sure the password string it is passed is strong. A strong password is defined 
as one that is at least eight characters long, contains both uppercase and lowercase characters, and has at least one digit. You may 
need to test the string against multiple regex patterns to validate its strength.'''

import re

password = input()

def strong_password(password):
    
    passwordRegex = re.compile(r'^[a-zA-Z0-9]{8,}$')
    mo = passwordRegex.search(password)
    
    if mo != None:
        mo_str = mo.group()
        for i in range(len(mo_str)):
            if mo_str[i].isdecimal():
                return 'That\'s your STRONG PASSWORD:' + mo.group().center(30) + ' Correct?'
            else:
                continue
        return 'Weak Password'
            
    else:
        return 'Weak Password'
print(strong_password(password))

# Regex Version of strip()
'''Write a function that takes a string and does the same thing as the strip() string method. If no other arguments are passed other 
than the string to strip, then whitespace characters will be removed from the beginning and end of the string. Otherwise, the characters
specified in the second argument to the function will be removed from the string.'''

def stripper(first, second = ''):
    if second == '':
        return first.strip()
    else:
        stripperRegex = re.compile(second)
        return stripperRegex.sub('', first)

print(stripper('Agent Yinka is working with Agent Saurabh', 'Agent'))
