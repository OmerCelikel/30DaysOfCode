# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
"""visitors = ['Firefox', 'corrupted', 'Chrome', 'corrupted',
            'Safari', 'corrupted', 'Safari', 'corrupted',
            'Chrome', 'corrupted', 'Firefox', 'corrupted']


print("visitors[1::2] : ", visitors[1::2])
print("visitors[2::2]  : ", visitors[2::2])
print(visitors)
"""
# number of test cases
T = int(input())
if T < 2 and T > 10:
    sys.exit()

for words in range(0,T):
    word = input()
    print(word[0::2],word[1::2])

"""    print(word)
    oddList = []
    evenList = []
    print()
    for letter in range(0,len(word)):
        # It is even list
        if letter%2 == 0:
            evenList.append(word[letter])
        else:
            oddList.append(word[letter])
    print(evenList, oddList)"""



