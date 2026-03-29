# Quiz ID: Z75101
lst1 = []
while True:
    a = input('input a word: ')
    a = a.lower()
    if a == 'quit':
        break
    else:
        lst1.append(a)

if len(lst1) == len(set(lst1)):
    print('there were no duplicates')
else:
    print('there were duplicates')

#v2 if lower and upper case do count as diffrent strs here is the new version

# lst1 = []
# while True:
#     a = input('input a word: ')
#     ######a = a.lower()###### yes only this line is getting removed
#     if a == 'quit':
#         break
#     else:
#         lst1.append(a)
#
# if len(lst1) == len(set(lst1)):
#     print('there were no duplicates')
# else:
#     print('there were duplicates')