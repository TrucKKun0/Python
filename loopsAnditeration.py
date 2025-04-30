#For loop

nums = [1,2,3,4,5]
for num in nums: #loops through the list
    if num == 3:
        print('Found')
        #break #breaks the loop
        continue #skips the current iteration and continues to the next iteration

    print(num)
#Nested For loop
for num in nums:
    for letter in 'abc':
        print(num, letter)
#Range
for i in range(10):
    print(i)

#While loop

x= 0
while x < 10:
    if x == 5:
        break
    print(x)
    x += 1
