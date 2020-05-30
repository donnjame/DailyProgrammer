'''
Write a function that computes the list of the first 100 Fibonacci numbers. 
By definition, the first two numbers in the Fibonacci sequence are 0 and 1, 
and each subsequent number is the sum of the previous two. As an example, 
here are the first 10 Fibonnaci numbers: 0, 1, 1, 2, 3, 5, 8, 13, 21, and 34.

'''

def fib():
    number = [0,1]
    fibb = []
    tries = 100
    while tries >1 :
        for y in number[-2:]:
            fibb.append(y)
        number.append(sum(fibb[-2:]))
        tries -= 1
    print(number)