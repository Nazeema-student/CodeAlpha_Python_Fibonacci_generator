def fibonacci(n):    #Defining the function with name fibonacci and passing one argument using recusrive function.
    if n == 0:
        return 0 
    elif n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

n = int(input("Enter a number: "))
print(fibonacci(n))    



#Recusrive function is itself the process of calling the function again and again.

#Fibonacci series is the number of series in each number is sum of the preceeding two numbers. 0, 1, 1, 2,3,5......