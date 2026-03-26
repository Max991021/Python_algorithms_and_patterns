'''
*
**
***
****
*****
'''
# for i in range(10):
#     print("*"*i)

# for i in range(10):
#     for j in range(i):
#         print("*",end=' ')
#     print()
    
'''
  *
 **
***
'''
for i in range(10,0,-1):
    for j in range(i):
        print('*', end=" ")
    print()
'''
***
**
*
'''
  
  
'''
***
 **
  *
'''
for i in range(10,0,-1):
    for j in range(10-i):
        print(' ',end=" ")
        
    for z in range(i):
        print('*',end=" ")
    print()
'''
  *
 ***
*****
'''

# n = 3
# for i in range(n+1):
#     spaces = '  ' * (n - i)
#     stars = '* ' * i
#     print( stars+spaces)

n = 5

for i in range(n):
    if i == 0 or i ==n-1:
        for j in range(n):
            print("*", end=' ')
        print()
    else:
        print("* "+" "*6+"*")


for i in range(n):
    for j in range(n-i):
        print("*", end=' ')
    print()