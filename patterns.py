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
print('___________________________')
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
print('___________________________')
'''
  *
 ***
*****
'''

n = 5
for i in range(n):
    for j in range(i,n):
        print(' ',end=" ")
    for j in range(i):
        print('*',end=" ")
    for j in range(i+1):
        print("*", end=' ')
    print()
print('___________________________')
n = 5

for i in range(n):
    if i == 0 or i ==n-1:
        for j in range(n):
            print("*", end=' ')
        print()
    else:
        print("* "+" "*6+"*")
print('___________________________')

for i in range(n):
    for j in range(n-i):
        print("*", end=' ')
    print()
print('___________________________')    
'''

     *
    ***
   *****
'''

for i in range(n):
    for j in range(i,n):
        print(' ',end=" ")
    for j in range(i+1):
        print('*',end=" ")
    for j in range(i):
        print('*',end=" ")
    print()
print('___________________________')   

'''
*******
 *****
  ***
   *
'''

for i in range(n):
    for j in range(i+1):
        print(' ',end=" ")
    for j in range(i,n):
        print('*',end=' ')
    for i in range(i,n-1):
        print('*',end=' ')
    print()
print('___________________________')

'''
   *
  ***
 *****
*******
 *****
  ***
   *
'''

for i in range(n-1):
    for j in range(i,n):
        print(" ",end=" ")
    for j in range(i):
        print('*',end=" ")
    for j in range(i+1):
        print("*", end=" ")
    print()
for i in range(n):
    for j in range(i+1):
        print(' ',end=" ")
    for j in range(i,n):
        print('*',end=' ')
    for j in range(i,n-1):
        print('*',end=' ')
    print()