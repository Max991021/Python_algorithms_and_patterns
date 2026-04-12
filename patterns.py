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
print('___________________________')

'''
double hill
'''

for i in range(n-1):
    for j in range(i,n):
        print(" ",end=" ")
    for j in range(i):
        print('*',end=" ")
    for j in range(i+1):
        print("*", end=" ")
    
    for j in range(i,n-2):
        print("_",end=" ")
    for j in range(i,n-2):
        print('_',end=" ")
    for j in range(i):
        print('*',end=" ")
    for j in range(i+1):
        print("*", end=" ")
    print()
    
for i in range(n-1):
    for j in range(i,n):
        print(" ",end=" ")
    for j in range(i):
        print('*',end=" ")
    for j in range(i+1):
        print("*", end=" ")
    
    for j in range(i,n-2):
        print("_",end=" ")
    for j in range(i,n-2):
        print('_',end=" ")
    for j in range(i):
        print('*',end=" ")
    for j in range(i+1):
        print("*", end=" ")
    print()
    

'''
    *
   * *
  * * *
'''

n = 5
def dia(n):
    hi = []
    ho = []
    for i in range(1, n + 1):
        # Create the stars with a space after each one
        row_stars = "* " * i
        
        # Strip the very last trailing space so it centers perfectly
        row_stars = row_stars.strip()
        
        # Center it based on the width of the bottom row
        hi.append(row_stars.center(n * 2))
    print(hi)
    for i in range(n-1,0,-1):
        # Create the stars with a space after each one
        row_stars = "* " * i
        
        # Strip the very last trailing space so it centers perfectly
        row_stars = row_stars.strip()
        
        # Center it based on the width of the bottom row
        ho.append(row_stars.center(n * 2))
    j = '\n'.join(ho)
    return '\n'.join(hi)+'\n'+j
print(dia(5))
def right(n):
    results = ''
    for row in range(n):
        for col in range(n - row):
            results += '*'
        if row < n-1:
            results += '\n'
    return results
print(right(5))


def hallow(n):
    ho = []
    for row in range(1,n+1):
        for col in range(1,2*n):
            if col == n-row+1 or col== n+row -1 or row==n:
                ho.append('* '*i)
            else:
                ho.append(''*i)
        