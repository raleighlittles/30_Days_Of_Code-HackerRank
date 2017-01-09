# Enter your code here. Read input from STDIN. Print output to STDOUT

def factorial(n):
    if n == 1:
        return 1
    else:
        return (n * factorial(n-1))
    

user_input = input()
print factorial(user_input)