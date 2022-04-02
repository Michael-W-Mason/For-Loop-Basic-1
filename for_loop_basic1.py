#1.) print all integers from 0- 150
print("First Challenge")
for i in range(0, 151):
    print(i)

#2.) print all multilpes of 5 from 5 - 1000
print("Second Challenge")
for i in range(5, 1001, 5):
    print(i)

#3.) Print integers 1-100. If divisible by 5 print conding instead, if divisible by 10 print Coding Dojo
print("Third Challenge")
for i in range(0, 101):
    if(i % 10 == 0):
        print("Coding Dojo")
    elif(i % 5 ==0):
        print("Coding")
    else:
        print(i)

#4.) add odd integers from 0 to 500,000
print("Fourth Challenge")
sum = 0
for i in range(0, 500001):
    if i % 2 != 0:
        sum += i
print(sum)

#5.) Print positive numbers starting at 2018 countding down by 4
print("Fifth Challenge")
for i in range(2018, 0, -4):
    if(i % 2 == 0):
        print(i)


""" 6.) Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that are a multiple of mult.
For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines) """
lowNum = 1
highNum = 1000
mult = 6
print("Sixth Challenge")
for i in range(lowNum, highNum + 1):
    if i % mult == 0:
        print(i)